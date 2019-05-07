from flask import Flask


def create_app():
    from . import routes
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/shelter_pets'
    routes.init_app(app)
    # services.init_app(app)
    return app
