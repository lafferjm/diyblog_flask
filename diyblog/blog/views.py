from flask import render_template
from . import bp
from diyblog.models import User, BlogPost, BlogComment


@bp.route('/')
def index():
    num_authors = User.query.count()
    num_posts = BlogPost.query.count()
    num_comments = BlogComment.query.count()

    stats = {
        'num_authors': num_authors,
        'num_posts': num_posts,
        'num_comments': num_comments
    }

    return render_template('blog/index.html', stats=stats)
