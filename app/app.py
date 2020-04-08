from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email  # required for validation routines

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysupersecretKEY'  # USED TO ECRYPT SESSION COOKIES, must be diffeent for apps


class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[DataRequired(), Email()])  # label, validations
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@app.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    message = ''

    if form.is_submitted():
        if form.validate_on_submit():
            message = 'Valid'
        else:
            message = 'Invalid'

    return render_template('login/index.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
