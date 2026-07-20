from pydantic import BaseModel, EmailStr, UUID4, Field
from typing import Optional

class UserRegisterRequest(BaseModel):
    """Валидация формы регистрации"""
    email: EmailStr = Field(..., examples=["anna_k@gmail.com"])
    username: str = Field(..., examples=["anna_k"])
    password: str = Field(..., examples=["supersecretpassword"])

class UserResponse(BaseModel):
    """Ответ на регистрацию"""
    id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    email: EmailStr = Field(..., examples=["anna_k@gmail.com"])
    username: str = Field(..., examples=["anna_k"])

class UserLoginRequest(BaseModel):
    """Валидация авторизации"""
    email: EmailStr = Field(..., examples=["anna_k@gmail.com"])
    password: str = Field(..., examples=["supersecretpassword"])

class TokenResponse(BaseModel):
    """Ответ на авторизацию"""
    access_token: str = Field(..., examples=["eyJhbGciOiJIUzI1NiIsIn..."])
    token_type: str = Field(..., examples=["bearer"])