from app.requests import request_quote
from . import main
from flask import render_template,request,redirect, render_template,flash,abort, url_for
from flask_login import login_required
from app.models import Comment
from . import *


@main.route('/', methods = ["GET", "POST"])
def index():
    title = "My Blog"
    quote = request_quote()
    
    return render_template('index.html', quote=quote, title=title)

@main.route('/about')
def about():
    title = "Myself"
    return render_template('about.html',title=title)