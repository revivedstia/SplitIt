FROM python:3.11-slim

WORKDIR /app

# Запрещаем Python писать файлы .pyc на диск и буферизировать вывод
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Запускаем uvicorn с флагом --reload для автоперезагрузки кода при изменениях
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]