# Вибір образу з Python та встановлення залежностей
FROM python:3.10-slim

# Встановлення робочої директорії
WORKDIR /app

# Копіюємо файл залежностей і встановлюємо їх
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копіюємо проект у Docker контейнер
COPY . .

# Виконання команд для запуску проекту
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
