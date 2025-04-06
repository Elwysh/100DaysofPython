from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")

app = Flask(__name__)

app.secret_key = "some secret string"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["Post", "Get"])
def login():
    form = MyForm()
    if form.validate_on_submit():       # checks if the form is POST or GET
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html', form=form)
        else:
            return render_template('denied.html', form=form)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
