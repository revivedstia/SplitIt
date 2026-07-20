from fastapi import APIRouter, status
from app.schemas.users import UserRegisterRequest, UserResponse, UserLoginRequest, TokenResponse

# router = APIRouter(prefix="/api/users", tags=["Users"])

# @router.post("")
# async def create_user():
#     """Создать нового участника"""
#     return {"message": "User created (stub)"}



router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, 
             summary="Регистрация нового пользователя")
async def register(payload: UserRegisterRequest):
    return {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "email": payload.email,
        "username": payload.username
    }

@router.post("/login", response_model=TokenResponse, summary="Вход в систему")
async def login(payload: UserLoginRequest):
    return {
        "access_token": "mock_jwt_token",
        "token_type": "bearer"
    }