from flask import Blueprint, request, jsonify
from app.models import db, User

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return "Привет с домашнего маршрута!"

@home_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@home_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201