from flask import Blueprint, request, jsonify

from database import db
from models.models import User, Post

post_bp = Blueprint('post', __name__)

@post_bp.route('/users/<int:user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    posts = Post.query.filter_by(user_id=user_id).all()
    return jsonify([post.to_dict() for post in posts])

@post_bp.route('/users/<int:user_id>/posts', methods=['POST'])
def create_post(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {"error": "User not found"}, 404
    post_data = request.get_json()
    new_post = Post(title=post_data.get('title'), content=post_data.get('content'), user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    return jsonify(new_post.to_dict()), 201