import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    PORT = int(os.getenv("PORT", 5000))
