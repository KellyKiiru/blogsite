from email.quoprimime import quote

from app.requests import request_quote
from . import main
from flask import render_template


@main.route('/')
def index():
    
    quote = request_quote()
    
    return render_template('index.html', quote=quote)