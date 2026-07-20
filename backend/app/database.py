from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

# Асинхронный движок
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Фабрика для создания сессий
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для всех будущих моделей БД
class Base(DeclarativeBase):
    pass

# Зависимость для FastAPI (Dependency Injection)
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session