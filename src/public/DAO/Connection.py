import mysql.connector as connector
import src.public.DAO.Sensitive as private

#Classe to connection to the database
class Connection:

    DB_HOST = private.DB_HOST
    DB_NAME = private.DB_NAME
    DB_USER = private.DB_USER
    DB_PASSWORD = private.DB_PASSWORD

    def getConnection(self):

        try:
            conn = connector.connect(host=self.DB_HOST,
                                     database=self.DB_NAME,
                                     user=self.DB_USER,
                                     password=self.DB_PASSWORD
                                     )

            if conn.is_connected():
                cursor = conn.cursor()
                cursor.execute('select database();')
                record = cursor.fetchone()
                print(f'You are connected to database: {record}')

            return conn

        except ConnectionError as e:
            print(e)

