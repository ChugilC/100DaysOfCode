from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)

class TodoForm(FlaskForm):
    todo = StringField("Enter your todo", validators=[DataRequired()])
    submit = SubmitField("Submit")


all_todos = []

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TodoForm
    if form.validate_on_submit():
        my_todo = form.todo.data
        all_todos.append(my_todo)

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)