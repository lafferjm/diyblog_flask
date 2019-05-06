from datetime import datetime
from flask_user import UserMixin
from diyblog import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User authentication fields
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean())
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    bio = db.Column(db.String(400))

    roles = db.relationship('Role', secondary='user_roles', backref='roles')


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    author = db.relationship('User')
    author_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    content = db.Column(db.String(2000))
    post_date = db.Column(db.DateTime, default=datetime.utcnow)


class BlogComment(db.Model):
    __tablename__ = 'blog_comments'
    id = db.Column(db.Integer(), primary_key=True)
    comment = db.Column(db.String(1000))
    author_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    author = db.relationship('User')
    post_date = db.Column(db.DateTime(), default=datetime.utcnow)
    blog_id = db.Column(db.Integer(), db.ForeignKey('blog_posts.id'))
    blog = db.relationship('BlogPost', cascade='delete')

