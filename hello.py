from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
now = datetime.now()

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    now = datetime.now()
    date_time = now.strftime("%A, %B %-d, %Y %H:%M PM")
    return render_template('index.html', name = "Romil!", date_time=date_time)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    
if __name__ == '__main__':    
    app.run(debug=True)

