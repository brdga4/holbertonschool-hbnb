from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager


bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from app.api.v1 import blueprint as api_v1_blueprint

    app.register_blueprint(api_v1_blueprint)
    bcrypt.init_app(app)
    jwt.init_app(app)
    return app
