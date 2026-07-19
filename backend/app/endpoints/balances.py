from fastapi import APIRouter
from app.schemas.balances import GroupBalanceResponse, GlobalBalanceResponse

router = APIRouter()

@router.get("/groups/{group_id}/balances", response_model=GroupBalanceResponse, summary="Расчет долгов внутри конкретной группы")
async def get_group_balances(group_id: int):
    return {
        "group_id": group_id,
        "debts": [
            {
                "from_user": {"id": 2, "display_name": "Саша"},
                "to_user": {"id": 1, "display_name": "Аня"},
                "amount": 2000.00
            }
        ]
    }

@router.get("/balances/global", response_model=GlobalBalanceResponse, summary="Консолидированный глобальный баланс со всеми людьми")
async def get_global_balances():
    return {
        "user_id": 1,
        "global_balances": [
            {
                "user": {"id": 2, "display_name": "Саша"},
                "status": "you_owe",
                "amount": 100.00
            },
            {
                "user": {"id": 3, "display_name": "Ваня"},
                "status": "owes_you",
                "amount": 500.00
            }
        ]
    }