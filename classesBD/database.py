import pymysql
from classes.user import User

class Database:
    def __init__(self, host, port, user, password, db_name):
        self.connection = pymysql.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = db_name,
            cursorclass = pymysql.cursors.DictCursor
        )

    def add_user(self, username, password_hash, first_name, last_name, registered_at):
        insert_query = f"INSERT INTO `user` (username, password_hash, first_name, last_name, registered_at) VALUES ('{username}', '{password_hash}', '{first_name}', '{last_name}', '{registered_at}');" 

        with self.connection.cursor() as cursor:
            cursor.execute(insert_query)
            self.connection.commit()

    def search_username(self, username):
        select_query = f"SELECT * FROM 'user' WHERE username = '{username}';"

        with self.connection.cursor() as cursor:
            exist = cursor.execute(select_query)
            user = cursor.fetchone()

            self.connection.commit()  

            return user
        
    def username_password(self, username, password_hash):
        select_query = f"SELECT * FROM 'user' WHERE username = {username} and password = {password_hash};"

        with self.connection.cursor() as cursor:
            exist = cursor.execute(select_query)
            self.connection.commit()  

            return exist


    def __del__(self):
        self.connection.close()