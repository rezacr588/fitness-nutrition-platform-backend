from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    cors.init_app(app)

    # Import and register blueprints
    from app.apis.user_profiles import user_profiles_bp
    app.register_blueprint(user_profiles_bp)

    from app.apis.fitness_tracking import fitness_tracking_bp
    app.register_blueprint(fitness_tracking_bp)

    from app.apis.nutrition_tracking import nutrition_tracking_bp
    app.register_blueprint(nutrition_tracking_bp)

    # Import models
    from app.models import user_models, fitness_models, nutrition_models

    return app