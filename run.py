import os
from app import create_app

from dotenv import load_dotenv
dotenv_path = join(dirname(___file__), '.env')
load_dotenv(dotenv_path)

config_name = os.getenv('FLASK_ENV') or 'production'
app = create_app(config_name)
