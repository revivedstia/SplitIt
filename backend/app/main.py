from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import auth, groups, expenses, transfers, balances

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ПРИ ЗАПУСКЕ 
    print("\n" + "="*50)
    print("SplitIt API успешно запущен в Docker.")
    print("Документация (Swagger): http://localhost:8000/docs")
    print("Альтернативная дока (Redoc): http://localhost:8000/redoc")
    print("="*50 + "\n")
    yield
    # ПРИ ВЫКЛЮЧЕНИИ 
    print("SplitIt API остановлен.")

app = FastAPI(
    title="SplitIt API", 
    lifespan=lifespan,
    version="1.0.0",
    description="SplitIt - Expense tracking service"
)

# Настройка CORS для работы с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене заменить на конкретный URL фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Подключение роутеров
app.include_router(auth.router, prefix="/api/auth", tags=["Аутентификация (Auth)"])
app.include_router(groups.router, prefix="/api/groups", tags=["Группы (Groups)"])
app.include_router(expenses.router, prefix="/api/groups", tags=["Траты (Expenses)"])
app.include_router(transfers.router, prefix="/api/groups", tags=["Переводы (Transfers)"])
app.include_router(balances.router, prefix="/api", tags=["Балансы и отчеты (Balances)"])

@app.get("/health")
async def health_check():
    return {"status": "healthy"}