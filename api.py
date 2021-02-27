from db import database, mycursor
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))    

@app.route('/home', methods= ["GET", "POST"])
def home(): 

    if request.method == "POST":
        my_title= request.form.get("title")
        my_link= request.form.get("video_link")
        my_category= request.form.get("category")
        print("MES DATAS", my_link, my_title, my_category)
        mycursor.execute("INSERT INTO Courses (CATEGORY, TITLE, LINK) VALUES (%s,%s,%s) ",(my_category, my_title, my_link) )

        database.commit()

    return render_template("index.html")

@app.route('/javascript', methods= ["GET"])
def javascript(): 
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'JavaScript';")
    result = mycursor.fetchall()
    print('request=', result)
    return render_template("javascript.html", len = len(result), results=result)


@app.route('/api/javascript')
def javascript_api():
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'JavaScript';")
    output = mycursor.fetchall()
    return jsonify(output)


@app.route('/python', methods= ["GET"])
def python(): 
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Python';")
    result = mycursor.fetchall()
    print('request=', result)
    return render_template("python.html", len = len(result), results=result)


@app.route('/api/python')
def python_api():
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Python';")
    output = mycursor.fetchall()
    return jsonify(output)



@app.route('/azure', methods=["GET"])
def azure():
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Azure'")
    output = mycursor.fetchall()
    return render_template("Azure.html", len= len(output), result= output)

@app.route('/api/azure')
def azure_api():
    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Azure'")
    output = mycursor.fetchall()
    return jsonify(output)

if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=3000, debug = True)
