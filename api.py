from db import database, mycursor
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))    

@app.route('/home')
def home(): 
    return render_template("index.html")

@app.route('/api/javascript')
def javascript():
    mycursor.execute("SELECT * FROM Javascript")
    output = mycursor.fetchall()
    return jsonify(output)

@app.route('/api/python')
def python():
    mycursor.execute("SELECT * FROM Python")
    output = mycursor.fetchall()
    return jsonify(output)

@app.route('/api/azure')
def azure():
    mycursor.execute("SELECT * FROM Azure")
    output = mycursor.fetchall()
    return jsonify(output)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=4200, debug = True)