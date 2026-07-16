from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.api.v1 import blueprint as api_v1_blueprint

    app.register_blueprint(api_v1_blueprint)

    return app
