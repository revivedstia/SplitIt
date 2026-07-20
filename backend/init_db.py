import asyncio
import sys
from app.database import engine, Base
# ВАЖНО: нужно импортировать модель User, чтобы SQLAlchemy 
# узнала о ее существовании и записала в реестр Base.metadata
from app.models.users import User 
from sqlalchemy.exc import OperationalError

async def init_models():
    print("Попытка подключения к базе данных и создание таблиц...")
    
    try:
        async with engine.begin() as conn:
            # УДАЛЕНИЕ таблиц и данных (Опционально)
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            
        print("Успех! Таблица 'users' успешно создана в PostgreSQL.")

    except Exception as e:
        print(f"Ошибка подключения к базе данных: \n {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Запускаем асинхонную функцию в обычном Python-скрипте
    asyncio.run(init_models())