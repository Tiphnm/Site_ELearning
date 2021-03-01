import mysql.connector
import logging 

logging.basicConfig(filename='logging.log', level=logging.INFO,
                    format='%(asctime)s: %(name)s :%(levelname)s:%(message)s')

logging.info('This is an info:')
logging.error('This is an error:')

database = mysql.connector.connect(
                                host="mysql_db",
                                database= "My_classes",
                                user="elearning_user",
                                port="3306",
                                password="123"
                                )

mycursor= database.cursor()

def create_table():
    logging.info("Creating Table: start")
    mycursor.execute("CREATE TABLE IF NOT EXISTS Courses (ID INT PRIMARY KEY AUTO_INCREMENT, CATEGORY VARCHAR(255), TITLE VARCHAR(255), LINK VARCHAR(255));")
    logging.info("Creating Table: end")
create_table()

#mycursor.execute('INSERT INTO Javascript (TITLE, LINK) VALUES ("Mon titre", "Mon lien")')
#database.commit()
        
