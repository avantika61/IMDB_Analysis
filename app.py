from flask import Flask, request, render_template
import os
import pandas as pd
from src import *


app = Flask(__name__)
# Specify the file path of the CSV file
file_path = "titles.csv"
# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)
# Display the first few rows of the DataFrame
print(df.head())

@app.route("/")
def index_page():
    return index_handler(df)


if __name__=='__main__':
    app.run(debug=True)
