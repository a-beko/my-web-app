from flask import Flask
from config.settings import Config
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Инициализируем БД
    db.init_app(app)
    
    # Создаём таблицы (при первом запуске)
    with app.app_context():
        db.create_all()
    
    from app.routes.home import home_bp
    app.register_blueprint(home_bp)
    
    return app