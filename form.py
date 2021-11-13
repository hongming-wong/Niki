"""Autogenerates and accepts forms input"""

from flask import Flask

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)
my_choices = [('1', 'Cambodia'), ('2', 'China'), ('3', 'USA')]

class NameForm(FlaskForm):
    
    destinations = SelectMultipleField(choices=my_choices,validators=[DataRequired()], label="Where would you like to travel?")
		vaccinated = BooleanField("Are you vaccinated?", validators=[DataRequired()])
		budget = IntegerField("How much are you willing to spend?")
    name = StringField('Do you have any other suggestions?')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    names = [1, 2, 3, 4]
    # you must tell the variable 'form' what you named the class, above
    # 'form' is the variable name used in this template: index.html
    form = NameForm()
    message = ""
    if form.validate_on_submit():
        # redirect the browser to another route and template
        print(form.destinations.data)
        print(form.vaccinated.data)
        return redirect(
            "https://upload.wikimedia.org/wikipedia/en/4/4a/Dr_John_Zoidberg.png"
        )
    else:
        return render_template('index.html',
                               names=names,
                               form=form,
                               message=message)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# keep this as is
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
