from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTExtended
from flask_sqlalchemy import SQLAlchemy
from server.config import Config

db = SQLAlchemy()
jwt = JWTExtended()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from server.controllers.auth_controller import auth_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.guest_controller import guest_bp
    from server.controllers.appearance_controller import appearance_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(guest_bp)
    app.register_blueprint(appearance_bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)