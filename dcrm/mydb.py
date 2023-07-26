# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python 

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Akshat@890',

)


cursorObject = database.cursor()


cursorObject.execute('CREATE DATABASE elderco')



print('ALl done')
