from pydantic import BaseModel, Field, UUID4
from decimal import Decimal
from datetime import datetime

class TransferCreateRequest(BaseModel):
    """Фиксация перевода"""
    sender_id: UUID4 = Field(..., examples=["987f6543-e21b-73d3-b456-426614174111"])  # Кто отдал
    recipient_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"]) # Кому отдал
    amount: Decimal = Field(..., examples=[2000.00])

class TransferResponse(BaseModel):
    """Бэк подтверждает фиксацию перевода"""
    id: UUID4 = Field(..., examples=["a10e8400-e29b-41d4-a716-446655442222"])
    group_id: UUID4 = Field(..., examples=["660e8400-e29b-41d4-a716-446655441111"])
    sender_id: UUID4 = Field(..., examples=["987f6543-e21b-73d3-b456-426614174111"])
    recipient_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    amount: Decimal = Field(..., examples=[2000.00])
    created_at: datetime