from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from server.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import and register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)

    @app.route('/')
    def index():
        return {
            "message": "Welcome to the Late Show API",
            "endpoints": {
                "GET /guests": "List all guests",
                "GET /episodes": "List all episodes",
                "GET /episodes/<id>": "Get episode by ID",
                "DELETE /episodes/<id>": "Delete episode by ID (requires JWT)",
                "POST /appearances": "Create an appearance (requires JWT)",
                "POST /register": "Register a new user",
                "POST /login": "User login"
            }
        }

    return app
