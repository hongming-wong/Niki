"""Autogenerates and accepts forms input"""
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, RadioField, SelectMultipleField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms_components import DateRange
from replit import db
from datetime import date
import json

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

# form variables
my_choices = [('1', 'Cambodia'), ('2', 'China'), ('3', 'USA')]
budgetMin = 1000
startDate = date.today()



class NameForm(FlaskForm):
    name = StringField("Your name?", validators=[DataRequired()])
    destinations = SelectMultipleField(choices=my_choices, validators=[DataRequired()], label="Where would you like to travel?")
    vaccinated = BooleanField("Are you vaccinated?",validators=[DataRequired()])
    budget = IntegerField("How much are you willing to spend?", validators=[DataRequired(), NumberRange(min=budgetMin)])
		#note that wtf forms don't offer selection of range of dates
		# this is temporary! 
    start_date = DateField(label = "When onwards will you be available?", validators=[DateRange(min=startDate)])
    suggestions = StringField('Do you have any other suggestions?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    names = [1, 2, 3, 4]
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    if form.validate_on_submit():
        # stores the information in the database
        if "count" in db.keys():
            db["count"] = db["count"] + 1
        else:
            db["count"] = 1
        dictionary = {"destinations": form.destinations.data, 
        "vaccinated": form.vaccinated.data,
        "budget": form.vaccinated.data,
        "date": form.start_date.data.strftime("%Y/%m/%d"),
        "suggestions": form.suggestions.data
        }
        json_object = json.dumps(dictionary, indent = 4, default=str)
        db[form.name.data] = json_object 
        # redirect the browser to another route and template
        return redirect(
            "https://upload.wikimedia.org/wikipedia/en/4/4a/Dr_John_Zoidberg.png"
        )
    else:
        return render_template('index.html',
                               names=names,
                               form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
