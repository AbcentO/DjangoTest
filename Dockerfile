# Используем базовый образ Python
FROM python:3.8

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущего каталога в рабочую директорию контейнера
COPY . .

# Запускаем сервер Django
CMD python manage.py runserver
