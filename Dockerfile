FROM python:3.12.3

# Установка рабочей директории
WORKDIR /app

# Копирование файлов проекта
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]