from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, length
from flask_wtf.file import FileField, FileRequired, FileAllowed


class NewBlogPost(FlaskForm):
    author = StringField('Author', validators=[DataRequired(), length(max=30)])
    title = StringField('Title', validators=[DataRequired(), length(max=150)])
    content = TextAreaField('Content', validators=[DataRequired()])
    cover_image = FileField('Cover image',validators=[FileRequired(), FileAllowed(['jpg', 'jpeg' 'png'], 'Images only!')])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    username = StringField('', validators=[DataRequired(), length(max=30)])
    comment = TextAreaField('Write Your Comment', validators=[DataRequired(), length(max=100)])
    submit = SubmitField('comment')
