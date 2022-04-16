from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'

db = SQLAlchemy(app)
class posts(db.Model):
   id = db.Column('post_id', db.Integer, primary_key = True)
   uuid = db.Column(db.String(50))
   text = db.Column(db.Text)
   ip = db.Column(db.String(50))

def __init__(self, uuid, text, ip):
   self.uuid = uuid
   self.text = text
   self.ip = ip

db.create_all()

@app.route('/')
def hello_world():  # put application's code here
    return '<a href="/new-item">Write Post</a>'

@app.route('/ip')
def get_ip():
    return request.remote_addr

@app.route('/ip1')
def get_ip1():
    return request.environ['REMOTE_ADDR']

@app.route('/new-item', methods=['GET', 'POST'])
def new_item():
    if request.method == 'POST':
        # Form being submitted; grab data from form.
        text_form = request.form['text_form']
        # url = request.form['url']
        print(text_form)
        return text_form
    else:
        return render_template('write-post.html')

if __name__ == '__main__':
    app.run()
