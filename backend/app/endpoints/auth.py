from fastapi import APIRouter, status
from backend.app.schemas.users import UserRegisterRequest, UserResponse, UserLoginRequest, TokenResponse

# router = APIRouter(prefix="/api/users", tags=["Users"])

# @router.post("")
# async def create_user():
#     """Создать нового участника"""
#     return {"message": "User created (stub)"}



router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED, summary="Регистрация нового пользователя")
async def register(payload: UserRegisterRequest):
    return {
        "id": 1,
        "username": payload.username,
        "display_name": payload.display_name
    }

@router.post("/login", response_model=TokenResponse)
async def login(payload: UserLoginRequest):
    """Вход в систему"""
    return {
        "access_token": "mock_jwt_token_for_sasha",
        "token_type": "bearer"
    }