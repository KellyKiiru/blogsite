from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Quote:
    def __init__(self,author,quote):
        self.author=author,
        self.quote=quote

class User(UserMixin, db.Model):
    __tablename__ = 'authors'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    pass_secure = db.Column(db.String, nullable=False)
    profile_path = db.Column(db.String, nullable=True)

    @property
    def password(self):
        return AttributeError('You cannot read passwords')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def get_id(self):
        return self.user_id


class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    comment = db.Column(db.String, nullable=False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

class Upvote():
    pass
class Downvote():
    pass