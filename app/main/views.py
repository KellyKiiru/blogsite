from app.requests import request_quote
from . import main
from flask import render_template


@main.route('/')
def index():
    title = "My Blog"
    quote = request_quote()
    
    return render_template('index.html', quote=quote, title=title)

@main.route('/about')
def about():
    title = "Myself"
    return render_template('about.html',title=title)
    