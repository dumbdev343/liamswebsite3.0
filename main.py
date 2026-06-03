#!/usr/bin/python3

from flask import Flask, render_template, request
import os
import time


app = Flask(__name__)

@app.route("/")
def route1():
    return render_template("index.html")
@app.route("/abmt")
def route2():
    return render_template("abmt.html")

if __name__ == "__main__":
    app.run(debug=True)
