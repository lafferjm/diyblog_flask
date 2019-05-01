from flask import Blueprint

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def index():
    return 'Blog Index'
