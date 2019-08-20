from flask import Flask
from config import app_config, Config

def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # module inits

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    # blueprint registration

    if not app.debug and not app.testing:
        pass
        # production logging

    return app
