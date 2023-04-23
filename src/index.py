from flask import render_template
import pandas as pd

def index_handler(df):
    movie_count = df[df["type"] == "MOVIE"].shape[0]
    show_count = df[df["type"] == "SHOW"].shape[0]
    movie_show_response = [{"type":"Movie","total":movie_count, "color":"#E50914"},{"type":"Show","total":show_count,"color":"#430000"}]
    print(movie_show_response)
    return render_template('index.html', movie_show_response=movie_show_response)
