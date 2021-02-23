import mysql.connector

database = mysql.connector.connect(
                                host="localhost",
                                database= "My_classes",
                                user="root",
                                password="123")

mycursor= database.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS Javascript (ID INT PRIMARY KEY AUTO_INCREMENT, TITLE VARCHAR(255), LINK VARCHAR(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Python (ID INT PRIMARY KEY AUTO_INCREMENT, TITLE VARCHAR(255), LINK VARCHAR(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Azure (ID INT PRIMARY KEY AUTO_INCREMENT, TITLE VARCHAR(255), LINK VARCHAR(255));")

create_table()

#mycursor.execute('INSERT INTO Javascript (TITLE, LINK) VALUES ("Mon titre", "Mon lien")')
#database.commit()
        
