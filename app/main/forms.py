from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, length


class NewBlogPost(FlaskForm):
    author = StringField('Author', validators=[DataRequired(), length(max=40)])
    title = StringField('Title', validators=[DataRequired(), length(max=140)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('submit')


class CommentForm(FlaskForm):
    username = StringField('', validators=[DataRequired(), length(max=30)])
    comment = TextAreaField('Comment, Complaint, Compliment', validators=[DataRequired(), length(max=280)])
    submit = SubmitField('comment')
