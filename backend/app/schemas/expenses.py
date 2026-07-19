from pydantic import BaseModel, Field, UUID4
from decimal import Decimal
from datetime import datetime
from typing import List

class ExpenseCreateRequest(BaseModel):
    """Валидация траты"""
    title: str = Field(..., examples=["Пицца"])
    amount: Decimal = Field(..., examples=[1560.90])  
    payer_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    excluded_ids: List[UUID4] = Field(None, examples=[
        "123e4567-e89b-12d3-a456-426614174000", 
        "987f6543-e21b-73d3-b456-426614174111"
    ])

class ExpenseResponse(BaseModel):
    """Ответ: детали только что сохраненной траты"""
    id: UUID4 = Field(..., examples=["550e8400-e29b-41d4-a716-446655440000"])
    group_id: UUID4 = Field(..., examples=["660e8400-e29b-41d4-a716-446655441111"])
    title: str = Field(..., examples=["Пицца"])
    amount: Decimal = Field(..., examples=[6000.00])
    payer_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    participant_ids: List[UUID4] = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    created_at: datetime

class ExpenseHistoryResponse(BaseModel):
    """Запросистории расходов группы"""
    id: UUID4 = Field(..., examples=["550e8400-e29b-41d4-a716-446655440000"])
    title: str = Field(..., examples=["Крепкий алкоголь на тусовку"])
    amount: Decimal = Field(..., examples=[6000.00])
    payer_username: str = Field(..., examples=["anna_k"])  # Сразу имя вместо ID
    participants_count: int = Field(..., examples=[3])     # Количество человек в чеке
    created_at: datetime