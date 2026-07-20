from fastapi import APIRouter, status
from typing import List
from app.schemas.expenses import ExpenseCreateRequest, ExpenseResponse, ExpenseHistoryResponse
from datetime import datetime

router = APIRouter()

@router.post("/{group_id}/expenses", response_model=ExpenseResponse, status_code=status.HTTP_201_CREATED, summary="Добавление новой траты")
async def create_expense(group_id: int, payload: ExpenseCreateRequest):
    return {
        "id": 101,
        "group_id": group_id,
        "title": payload.title,
        "amount": payload.amount,
        "payer_id": payload.payer_id,
        "participant_ids": payload.participant_ids,
        "created_at": datetime.utcnow()
    }

@router.get("/{group_id}/expenses", response_model=List[ExpenseHistoryResponse], summary="История трат группы")
async def get_expense_history(group_id: int):
    return [
        {
            "id": 101,
            "title": "Крепкий алкоголь на тусовку",
            "amount": 6000.00,
            "payer_name": "Аня",
            "participants_count": 3,
            "created_at": datetime.utcnow()
        }
    ]