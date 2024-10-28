import mysql.connector

class DatabaseConnection:
    def connect_to_database(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="expensetracker"
        )
        return conn

