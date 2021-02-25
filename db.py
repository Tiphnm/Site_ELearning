import mysql.connector

database = mysql.connector.connect(
                                host="localhost",
                                database= "My_classes",
                                user="root",
                                password="123")

mycursor= database.cursor()

def create_table():
    mycursor.execute("CREATE TABLE IF NOT EXISTS Courses (ID INT PRIMARY KEY AUTO_INCREMENT, CATEGORY VARCHAR(255), TITLE VARCHAR(255), LINK VARCHAR(255));")

create_table()

#mycursor.execute('INSERT INTO Javascript (TITLE, LINK) VALUES ("Mon titre", "Mon lien")')
#database.commit()
        
