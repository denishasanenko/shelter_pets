from .shelter import shelter_bp


def init_app(app):
    app.register_blueprint(shelter_bp)
