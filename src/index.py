from flask import render_template

def index_handler():
    return render_template('index.html')
