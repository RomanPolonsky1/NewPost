from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4
import Posts

app = Flask(__name__)

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
        item = Posts.insert_new_post(text_form, request.remote_addr)
        return text_form + item.get_uuid()
    else:
        return render_template('write-post.html')


@app.route('/<string:url>')
def get_post(url):
    post = Posts.get_post(url)
    return post


if __name__ == '__main__':
    app.run()
