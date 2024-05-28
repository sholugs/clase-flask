from flask import Blueprint, render_template
from models.models import User

views_bp = Blueprint('views', __name__)

@views_bp.route('/', methods=['GET'])
def home():
    # users = User.query.all()
    return render_template('index.html')