from flask import Flask, request, render_template
import os
from src import *


app = Flask(__name__)

@app.route("/")
def index_page():
    return index_handler()


if __name__=='__main__':
    app.run(debug=True)