from fastapi import APIRouter, status
from typing import List
from app.schemas.groups import GroupCreateRequest, GroupResponse, AddMemberRequest, AddMemberResponse
from datetime import datetime

router = APIRouter()

@router.post("", response_model=GroupResponse, status_code=status.HTTP_201_CREATED, summary="Создание новой группы")
async def create_group(payload: GroupCreateRequest):
    return GroupResponse({
        "id": 10,
        "name": payload.name,
        "description": payload.description,
        "created_at": datetime.utcnow()
    })

# @router.get("", response_model=List[GroupResponse], summary="Получение списка групп текущего пользователя")
# async def get_groups():
#     return [
#         {"id": 10, "name": "Поездка в Питер", "description": "Расходы на выходные", "created_at": datetime.utcnow()},
#         {"id": 11, "name": "Наша квартира", "description": "Совместное проживание", "created_at": datetime.utcnow()}
#     ]

@router.post("/{group_id}/members", response_model=AddMemberResponse, summary="Добавление участника в группу")
async def add_member(group_id: int, payload: AddMemberRequest):
    return {
        "group_id": group_id,
        "user_id": 2,
        "username": payload.username,
        "display_name": "Саша"
    }