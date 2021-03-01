from db import database, mycursor, logging
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome(): 
    return redirect(url_for('home'))    


@app.route('/home', methods= ["GET", "POST"])
def home(): 
    logging.info("Launching homepage: start")

    if request.method == "POST":
        my_title= request.form.get("title")
        my_link= request.form.get("video_link")
        my_category= request.form.get("category")
        print("MES DATAS", my_link, my_title, my_category)
        mycursor.execute("INSERT INTO Courses (CATEGORY, TITLE, LINK) VALUES (%s,%s,%s) ",(my_category, my_title, my_link) )
        database.commit()

    logging.info("Launching homepage: end")

    return render_template("index.html")


@app.route('/javascript', methods= ["GET"])
def javascript(): 
    logging.info("Launching javascript page: start")

    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'JavaScript';")
    result = mycursor.fetchall()
    print('request=', result)

    logging.info("Launching javascript page: end")

    return render_template("javascript.html", len = len(result), results=result)


# @app.route('/api/javascript')
# def javascript_api():
#     logging.info("Launching javascript API page: start")

#     mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'JavaScript';")
#     output = mycursor.fetchall()

#     logging.info("Launching javascript API page: end")

#     return jsonify(output)


# @app.route('/api/python')
# def python():
#     logging.info("Launching python API page: start")

#     mycursor.execute("SELECT * FROM Courses")
#     output = mycursor.fetchall()

#     logging.info("Launching python API page: end")

#     return jsonify(output)


@app.route('/azure', methods=["GET"])
def azure():
    logging.info("Launching azure page: start")

    mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Azure'")
    output = mycursor.fetchall()
    logging.info("Launching azure page: end")

    return render_template("Azure.html", len= len(output), result= output) 


# @app.route('/api/azure')
# def azure_api():
#     logging.info("Launching Azure API page: start")

#     mycursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Azure'")
#     output = mycursor.fetchall()
#     logging.info("Launching Azure API page: end")

#     return jsonify(output)


if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=4200, debug = True)