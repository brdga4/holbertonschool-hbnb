from flask import Blueprint
from flask_restx import Api
from app.api.v1.amenities import api as amenities_ns


blueprint = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(
    blueprint,
    title='HBnB API',
    version='1.0',
    description='HBnB Application API'
)

api.add_namespace(amenities_ns, path='/amenities')
