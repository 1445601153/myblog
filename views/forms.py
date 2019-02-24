from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):  # Testify
    name = StringField("What's your name? ", validators=[DataRequired()])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):  # login form
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
