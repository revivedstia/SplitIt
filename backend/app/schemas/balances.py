from pydantic import BaseModel, Field, UUID4
from decimal import Decimal
from typing import List

class UserShortInfo(BaseModel):
    """Вспомогательный класс: отдает минимум инфы о пользователе внутри отчетов"""
    id: UUID4 = Field(..., examples=["987f6543-e21b-73d3-b456-426614174111"])
    username: str = Field(..., examples=["anna_k"])

class DebtInfo(BaseModel):
    """Вспомогательный класс: описывает одну пару должник -> кредитор"""
    from_user: UserShortInfo  # Кто должен
    to_user: UserShortInfo    # Кому должен
    amount: Decimal = Field(..., examples=[2000.00])

class GroupBalanceResponse(BaseModel):
    """Бэк отдает список оптимизированных долгов группы"""
    group_id: UUID4 = Field(..., examples=["660e8400-e29b-41d4-a716-446655441111"])
    debts: List[DebtInfo]    

class GlobalBalanceItem(BaseModel):
    """Вспомогательный класс: баланс с одним конкретным человеком по всем группам"""
    user: UserShortInfo
    status: str = Field(..., examples=["you_owe", "owes_you"]) # Вы должны или вам должны
    amount: Decimal = Field(..., examples=[100.00])

class GlobalBalanceResponse(BaseModel):
    """Бэк отдает общие итоги по всем группам сразу"""
    user_id: UUID4 = Field(..., examples=["123e4567-e89b-12d3-a456-426614174000"])
    global_balances: List[GlobalBalanceItem] # Схлопнутые долги со всеми знакомыми