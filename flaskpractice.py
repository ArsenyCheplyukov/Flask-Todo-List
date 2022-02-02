#import libraries
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

# configure flask
app = Flask(__name__)
#configure flask database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # can be sqlite:////tmp/test.db
db = SQLAlchemy(app)

# database class: create columns, initialize them, output data 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __repr__(self):
        return '<User %r >' % self.username

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('main_template.html')

if __name__ == "__main__":
    app.run(debug=True)