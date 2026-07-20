from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.users import User
from app.schemas.users import UserRegisterRequest, UserResponse, UserLoginRequest, TokenResponse
from app.core.security import hash_password, verify_password, create_access_token


router = APIRouter(prefix="/api/users", tags=["Users"])

# @router.post("")
# async def create_user():
#     """Создать нового участника"""
#     return {"message": "User created (stub)"}


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, 
             summary="Регистрация нового пользователя")
async def register(payload: UserRegisterRequest, db: AsyncSession = Depends(get_db)):
    try:
        # проверяем уникальность email
        query = select(User).where(User.email == payload.email)
        result = await db.execute(query)
        existing_user = result.scalar_one_or_none()

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким логином или email уже существует"
            )

        new_user = User(
            username=payload.username,
            email=payload.email,
            password_hash=hash_password(payload.password)
        )

        db.add(new_user)
        await db.commit()
        await db.refresh(new_user) 

        return new_user  

    except HTTPException:
        raise 
    except Exception as e:
        print(f"Критическая ошибка при регистрации: \n {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка на стороне сервера при создании пользователя"
        )


@router.post("/login", response_model=TokenResponse, 
             summary="Вход в систему (получение токена)")
async def login(payload: UserLoginRequest, db: AsyncSession = Depends(get_db)):
    try:
        query = select(User).where(User.email == payload.email)
        result = await db.execute(query)
        user = result.scalar_one_or_none()

        if not user or not verify_password(payload.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверное имя пользователя или пароль"
            )

        access_token = create_access_token(data={"sub": str(user.id)})

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"Критическая ошибка при входе: \n {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка на стороне сервера при авторизации"
        )
    