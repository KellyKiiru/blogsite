from app.requests import request_quote
from . import main
from flask import render_template,request,redirect, render_template,flash,abort, url_for
from flask_login import login_required,current_user
from app.models import Posts, Comment, User
from . import *
from app import db
from .forms import NewBlogPost, CommentForm



@main.route('/')
def index():
    title = "My Blog"
    quote = request_quote()
    
    return render_template('index.html', quote=quote, title=title)

@main.route('/about')
def about():
    title = "Myself"
    return render_template('about.html',title=title)


@main.route('/add/<user_id>', methods=["GET", "POST"])
@login_required
def add_new_blog(user_id):
    form = NewBlogPost()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        image = form.cover_image.data
        content = form.content.data
        new_blogpost = Posts(author=author, title=title, content=content,user_id=current_user.user_id)
        db.session.add(new_blogpost)
        db.session.commit()

        flash('Post added ')

        return redirect(url_for('main.index'))

    return render_template('add_new_blog.html', form=form)


