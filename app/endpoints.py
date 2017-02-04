from api_endpoints import SendEmailResource
from api_endpoints import SimpleResource
from .extensions import api


def register_endpoints(app):
    """ connects flask_restful endpoints to the app """
    api.app = app

    api.add_resource(SimpleResource, '/')
    api.add_resource(SendEmailResource, '/0.1/send_email/')
