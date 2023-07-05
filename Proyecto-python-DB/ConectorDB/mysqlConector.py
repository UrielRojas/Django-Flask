import mysql.connector


def mysqlConnection():
     database = mysql.connector.connect(
          host = "127.0.0.1",
          port = "3307",
          user = "root",
          password = "",
          database= "master_python"
     )

     return database


