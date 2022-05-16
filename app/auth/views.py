from app import db
from . import auth
from app.models import User
from flask import render_template, request,redirect,flash,url_for
from .forms import RegistrationForm

@auth.route('/register')
def register():
    
    '''
    Render registration form
    '''
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
    return render_template('registrationform.html', form=registration_form)
