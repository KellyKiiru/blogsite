import email
from flask_login import login_required, login_user,LoginManager
from app import db
from . import auth
from app.models import User
from flask import render_template, request,redirect,flash,url_for,flash
from .forms import LoginForm, RegistrationForm

@auth.route('/register', methods=["GET", "POST"])
def register():
    
    '''
    Render registration form
    '''
    
    title = "Register"
    registration_form= RegistrationForm()
    
    if request.method == "POST":
        if registration_form.validate_on_submit():
            check_existing = User.query.filter_by(email=registration_form.email.data).first()

            if check_existing is None:
                email = registration_form.email.data
                first_name = registration_form.first_name.data
                last_name = registration_form.last_name.data
                password = registration_form.password.data

                new_user = User(email=email, first_name=first_name, last_name=last_name, password=password, )

                db.session.add(new_user)
                db.session.commit()

                flash("Signed up successfully")
                return redirect(url_for('auth.login'))
            else:
                flash("Email already registered. Please login")
        else:
            flash("Please fill all fields with valid data")
    return render_template('registrationform.html', form=registration_form, title=title)

@auth.route('/login', methods=["GET", "POST"])
def login():
    title = "Login to Acc"
    
    '''
    Render login form
    '''
    login_form = LoginForm()
    
    if request.method == "POST":
        if login_form.validate_on_submit():
            email= login_form.email.data
            password = login_form.email.data
            
            get_user = User.query.filter_by(email=email).first()
            
            if get_user and User.verify_password(get_user, password):
                login_user(get_user)
                flash("Successfully logged in",category="primary")
                return redirect(request.args.get('next') or url_for('main.index'))
            else:
                flash("Wrong details")
        else:
            flash("Fill in the specified fields")           
    
    
    return render_template('login.html', form=login_form, title=title)