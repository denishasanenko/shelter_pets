def init_app(app):
    from .shelter import shelter_bp
    app.register_blueprint(shelter_bp)
