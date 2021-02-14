from flask import Flask, render_template, redirect
import pandas as pd
import numpy as np

app = Flask(__name__)

name = input()

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/")