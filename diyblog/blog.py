from flask import Blueprint, render_template

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def index():
    num_authors = 0
    num_posts = 0
    num_comments = 0

    stats = {
        'num_authors': num_authors,
        'num_posts': num_posts,
        'num_comments': num_comments
    }

    return render_template('blog/index.html', stats=stats)
