from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "MySecretKey"

ADMIN_EMAIL = "admin@email.com"
ADMIN_PASS = "12345678"
# Create a Form Class
class MyForm(FlaskForm):
    email = StringField(label="What's your email", validators=[DataRequired()])
    password = PasswordField(label="What's your password", validators=[DataRequired()])
    submit = SubmitField("Log In")


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = None
    password = None
    form = MyForm()
    # Validate Form
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        if email == ADMIN_EMAIL and password == ADMIN_PASS:
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)