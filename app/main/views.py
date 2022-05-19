from app.requests import request_quote
from . import main
from flask import render_template,request,redirect, render_template,flash,abort, url_for
from flask_login import login_required,current_user
from app.models import Posts, Comment, User
from . import *
from app import db
from .forms import NewBlogPost, CommentForm
from sqlalchemy import desc



@main.route('/')
def index():
    title = "My Blog"
    posts = Posts.query.order_by(desc(Posts.created_on))
    quote = request_quote()
    
    return render_template('index.html', quote=quote, title=title, posts=posts)

@main.route('/indeks')
def indeks():
    posts = Posts.query.order_by(desc(Posts.created_on))

    quote = request_quote()
    return render_template('indeks.html', posts=posts, quote=quote)

@main.route('/about')
def about():
    title = "Myself"
    return render_template('about.html',title=title)


@main.route('/add/<user_id>', methods=["GET", "POST"])
@login_required
def add_blogpost(user_id):
    form = NewBlogPost()
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        content = form.content.data
        new_blogpost = Posts(author=author, title=title, content=content,user_id=current_user.user_id)
        db.session.add(new_blogpost)
        db.session.commit()

        flash('Post added ')

        return redirect(url_for('main.indeks'))

    return render_template('add_new_blog.html', form=form)

@main.route('/<post_title>/<post_id>', methods=['GET', 'POST'])
def read_post(post_title, post_id):
    post = Posts.query.filter_by(post_id=post_id).first()

    comment_form = CommentForm()

    post_comments = Comment.query.filter_by(post_id=post_id).all()

    if request.method == "POST":
        if comment_form.validate_on_submit():

            comment = comment_form.comment.data
            username = comment_form.username.data
            new_comment = Comment(comment=comment, post_id=post_id, username=username)

            Comment.save_comment(new_comment)

            return redirect(url_for('main.read_post', post_id=post_id, post_title=post_title, comments=post_comments))
        else:
            flash('Invalid comment. Remember, BE NICE')

    return render_template('post.html', post=post, comment_form=comment_form, comments=post_comments)

@main.route('/<post_id>', methods=["GET", "DELETE"])
@login_required
def delete_post(post_id):
    post_to_delete = Posts.query.filter_by(post_id=post_id).first()

    if post_to_delete:
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Post deleted successfully', category='success')
        return redirect(url_for('main.indeks'))
    else:
        pass

    return redirect(url_for('main.indeks'))

@main.route('/<post_title>/<post_id>/<comment_id>', methods=["GET", "DELETE"])
@login_required
def delete_comment(post_title, post_id, comment_id):
    comment_to_delete = Comment.query.filter_by(comment_id=comment_id).first()

    if comment_to_delete:
        db.session.delete(comment_to_delete)
        db.session.commit()
        flash('Comment deleted successfully', category='success')
        return redirect(url_for('main.read_post', post_title=post_title, post_id=post_id))
    else:
        pass

@main.route('/profile/<first_name>', methods=["GET", "POST"])
@login_required
def profile(first_name):
    posts = Posts.query.filter_by(user_id=current_user.user_id).all()

    print(posts)

    return render_template('profile.html', user=current_user, posts=posts)

@main.route('/update-post/<post_id>', methods=["GET", "POST"])
@login_required
def update_post(post_id):
    form = NewBlogPost()

    post = Posts.query.filter_by(post_id=post_id).first()

    if request.method == 'GET':
        form.author.data = post.author
        form.title.data = post.title
        form.content.data = post.content

    if post is None:
        abort(404)

    # Submission handling
    if request.method == "POST" and form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        content = form.content.data
        post.title = title
        post.author = author
        post.content = content
        db.session.commit()

        flash('Post updated successfully', category='success')

        return redirect(url_for('main.indeks'))

    return render_template('update-post.html', post=post, form=form)
