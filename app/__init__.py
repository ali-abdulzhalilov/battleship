from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # module inits

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # blueprint registration

    if not app.debug and not app.testing:
        pass
        # production logging

    return app
