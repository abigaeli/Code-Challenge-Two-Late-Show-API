from flask import Flask
from server.config import Config
from server.extensions import db, jwt, migrate

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
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(episode_bp, url_prefix='/episodes')
    app.register_blueprint(guest_bp, url_prefix='/guests')
    app.register_blueprint(appearance_bp, url_prefix='/appearances')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
