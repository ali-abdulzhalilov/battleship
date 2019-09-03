import os
from app import create_app

config_name = os.getenv('FLASk_ENV') or 'production'
app = create_app(config_name)
