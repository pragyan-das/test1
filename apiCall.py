# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 00:03:19 2022

@author: Pragyan
"""

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/test", methods = ['POST'])
def hello_world():
    if request.method == "POST":
     return "<h2>Hello, World!<h2>"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=5000)

