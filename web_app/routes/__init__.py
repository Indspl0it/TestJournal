from flask import Blueprint

from .user_routes import user_routes
from .journal_routes import journal_routes
from .question_routes import question_routes
from .mood_routes import mood_routes
from .image_routes import image_routes

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template('home.html')

def init_app(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(journal_routes)
    app.register_blueprint(question_routes)
    app.register_blueprint(mood_routes)
    app.register_blueprint(image_routes)
    app.register_blueprint(main)