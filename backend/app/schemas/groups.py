from pydantic import BaseModel, Field, UUID4, EmailStr
from datetime import datetime
from typing import Optional

class GroupCreateRequest(BaseModel):
    """Валидация формы создания группы"""
    title: str = Field(..., examples=["Поездка в Питер"])
    description: Optional[str] = Field(None, examples=["Поездака в июле на поезде втроем"])

class GroupResponse(BaseModel):
    """Ответ при создании группы"""
    id: UUID4 = Field(..., examples=["660e8400-e29b-41d4-a716-446655441111"])
    title: str = Field(..., examples=["Поездка в Питер"])
    description: Optional[str] = Field(None, examples=["Поездака в июле на поезде втроем"])
    created_at: datetime

class AddMemberRequest(BaseModel):
    """Добавление человека по его почте"""
    email: EmailStr = Field(..., examples=["anna_k@gmail.com"])

class AddMemberResponse(BaseModel):
    """Подтверждение, что человек успешно добавлен в группу"""
    group_id: UUID4 = Field(..., examples=["660e8400-e29b-41d4-a716-446655441111"])
    user_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    email: EmailStr = Field(..., examples=["anna_k@gmail.com"])