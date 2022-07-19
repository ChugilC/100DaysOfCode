from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

COFFEE_R = ['✘','☕️', '☕️☕️', '☕️☕️☕️','☕️☕️☕️☕️', '☕️☕️☕️☕️☕️']
POWER_R = ['✘','🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
WIFI_R = ['✘','💪', '💪💪', '💪💪💪','💪💪💪💪','💪💪💪💪💪']


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Location URL", validators=[DataRequired(), url()])
    open_time = StringField("Open Time", validators=[DataRequired()])
    close_time = StringField("Close Time", validators=[DataRequired()])
    coffee = SelectField("Coffee Ratings", choices=COFFEE_R)
    power = SelectField("Power Ratings", choices=POWER_R)
    wifi = SelectField("Wifi Ratings", choices=WIFI_R)
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("100 Days/Day-054/cafe-data.csv", mode="a", encoding="utf8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        print("Success")
        return redirect(url_for('cafes'), code=302)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('100 Days/Day-054/cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
