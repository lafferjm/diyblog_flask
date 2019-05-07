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

class BlogCommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired(), Length(max=1000)])
