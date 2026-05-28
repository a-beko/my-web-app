from flask import current_app

# Наши данные (как в примере с Node.js)
users = [
    {"id": 1, "name": "Bella"},
    {"id": 2, "name": "Admin"},
]


def get_db_connection():
    db_path = current_app.config.get("DB_PATH", "sqlite:///default.db")
    print(f"Connecting to database: {db_path}")
    return db_path


def get_all_users():
    """Возвращает список всех пользователей"""
    return users


def save_user(name, email):
    print(f"Saving user: {name}, {email}")
    return True
