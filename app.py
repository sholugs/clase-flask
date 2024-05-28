from flask import Flask
from database import db
from blueprints.user import user_bp
from blueprints.post import post_bp
from views.views import views_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(views_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5000)