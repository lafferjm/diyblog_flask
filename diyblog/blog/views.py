from flask import render_template, redirect, url_for
from . import bp
from .forms import BlogCreateForm
from diyblog.models import User, BlogPost, BlogComment
from diyblog import db


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

@bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = BlogCreateForm()
    form.author.choices = [(u.id, u.username) for u in User.query.order_by('username')]

    if form.validate_on_submit():
        blog_post = BlogPost(name=form.name.data, author_id=form.author.data, \
            content=form.content.data, post_date=form.post_date.data)
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html', form=form)

@bp.route('/blogs')
def blog_list():
    blogs = BlogPost.query.all()

    return render_template('blog/list_blogs.html', blogs=blogs)

@bp.route('/<int:blog_id>')
def blog_detail(blog_id):
    blog = BlogPost.query.filter_by(id=blog_id).first()

    return render_template('blog/detail_blog.html', blog=blog)

@bp.route('/bloggers')
def blog_author_list():
    authors = User.query.all()

    return render_template('blog/list_authors.html', authors=authors)
