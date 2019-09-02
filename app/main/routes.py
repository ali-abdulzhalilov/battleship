from flask import render_template, current_app
from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    is_testing = current_app.config['TESTING']
    return render_template('index.html', is_testing=is_testing)
