from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
bootstrap = Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email Address?', validators=[DataRequired(), validEmail])
    submit = SubmitField('Submit')

    

def validEmail(form, email):
        if email is not None and not email.find('@'):
            raise ValidationError(f'Please include an @ in the email address, {email} is missing @')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        if form.email.data is not None and not form.email.data.find('utoronto'):
            flash('Please fill in a UofT email')
        session['name'] = form.name.data
        # form.name.data = ''
        session['email'] = form.email.data
        # form.email.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', name = session.get('name'), form = form, email = session.get('email'))

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    
if __name__ == '__main__':    
    app.run(debug=True)

