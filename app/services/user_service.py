def get_welcome_message(username):
    # Это наша бизнес-логика
    return f"Welcome back, {username}!"


def calculate_discount(price, user_level):
    # Тоже бизнес-логика
    if user_level == "gold":
        return price * 0.8
    elif user_level == "silver":
        return price * 0.9
    return price
