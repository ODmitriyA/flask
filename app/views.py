from flask import render_template
from app import app


@app.route('/')
def index():
    message = 'Hello, Dmitriy!'
    return render_template(
        'message.html',
        message=message
    )
