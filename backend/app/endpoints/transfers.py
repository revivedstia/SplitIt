from fastapi import APIRouter, status
from app.schemas.transfers import TransferCreateRequest, TransferResponse
from datetime import datetime

router = APIRouter()

@router.post("/{group_id}/transfers", response_model=TransferResponse, status_code=status.HTTP_201_CREATED, summary="Фиксация возврата долга")
async def create_transfer(group_id: int, payload: TransferCreateRequest):
    return {
        "id": 50,
        "group_id": group_id,
        "sender_id": payload.sender_id,
        "recipient_id": payload.recipient_id,
        "amount": payload.amount,
        "created_at": datetime.utcnow()
    }