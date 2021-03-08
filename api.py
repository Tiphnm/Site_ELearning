import psycopg2, logging
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)


host = "rachid.postgres.database.azure.com"
dbname = "postgres"
user = "rachid@rachid"
password = "Leouf2017."
sslmode = "require"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(
    host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()





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
        cursor.execute("INSERT INTO Courses (CATEGORY, TITLE, LINK) VALUES (%s,%s,%s) ",(my_category, my_title, my_link) )
        database.commit()

    logging.info("Launching homepage: end")

    return render_template("index.html")


@app.route('/javascript', methods= ["GET"])
def javascript(): 
    logging.info("Launching javascript page: start")

    cursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'JavaScript';")
    result = cursor.fetchall()
    print('request=', result)

    logging.info("Launching javascript page: end")

    return render_template("javascript.html", len = len(result), results=result)


@app.route('/azure', methods=["GET"])
def azure():
    logging.info("Launching azure page: start")

    cursor.execute("SELECT * FROM Courses WHERE CATEGORY LIKE 'Azure'")
    output = mycursor.fetchall()
    logging.info("Launching azure page: end")

    return render_template("Azure.html", len= len(output), result= output) 




if __name__ == "__main__": 
    app.run(host= "0.0.0.0", port=4200, debug = True)
