from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<a href="/new-item">Write Post</a>'


@app.route('/new-item')
def new_item():
    return render_template('write-post.html')


if __name__ == '__main__':
    app.run()
