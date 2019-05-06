from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from diyblog.models import User

class BlogCreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    author = SelectField('Author', coerce=int)
    content = TextAreaField('Content', validators=[DataRequired(), Length(max=2000)])
    post_date = DateField('Post Date', validators=[DataRequired()])

#BlogComment
#     comment = db.Column(db.String(1000))
#     author_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
#     author = db.relationship('User')
#     post_date = db.Column(db.DateTime(), default=datetime.utcnow)
#     blog_id = db.Column(db.Integer(), db.ForeignKey('blog_posts.id'))
#     blog = db.relationship('BlogPost', cascade='delete')