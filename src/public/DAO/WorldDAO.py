import mysql.connector

from src.public.DAO.Connection import Connection
from tabulate import tabulate


class WorldDAO:

    def selectCity(self):

        connection = Connection()
        conn = connection.getConnection()

        try:

            query = """SELECT *FROM world.city;"""
            cursor = conn.cursor()
            cursor.execute(query)

            records = cursor.fetchall()
            print(f'Total number of rows in table: {cursor.rowcount}')

            print(tabulate(records, headers=['ID', 'Name', 'CountryCode', 'District', 'Population'],
                           tablefmt='fancy_grid'))

        except ConnectionError as e:
            print(e)

        finally:
            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')

    def selectCityID(self, id: int):

        connection = Connection()
        conn = connection.getConnection()

        try:

            query = f'SELECT *FROM world.city WHERE id = {id};'

            cursor = conn.cursor()
            cursor.execute(query)
            records = cursor.fetchmany()

            print(f'Total number of rows in table: {cursor.rowcount}')

            print(records)
            header = ['Name', 'CountryCode', 'District', 'Population']
            print(tabulate(records, headers=['ID', 'Name', 'CountryCode', 'District', 'Population'],tablefmt='fancy_grid'))
            # for row in records:
            #     print('-------------------------------------------')
            #     print(f'ID - {row[0]} | '
            #           f'Name - {row[1]} |'
            #           f'CountryCode - {row[2]} |'
            #           f'District - {row[3]} |'
            #           f'Population - {row[4]} \n')
            #

        except ConnectionError as e:
            print(e)

        finally:
            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')

    def createCity(self, name: str, country_code: str, district: str, population: int):

        connection = Connection()
        conn = connection.getConnection()

        try:

            query = """INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"""

            records = (name, country_code, district, population)
            cursor = conn.cursor()
            cursor.execute(query, records)
            conn.commit()

            print(f'Dados inseridos: {records}')

        except ConnectionError as e:
            print(e)

        finally:
            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')

    def delete(self, id: int):

        connection = Connection()
        conn = connection.getConnection()

        try:

            query = f'DELETE FROM world.city WHERE id = {id}'
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            print(f'ID {id} excluido com sucesso!')

        except ConnectionError as e:
            print('Failed to Delete: '.format(e))

        finally:

            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')

    def update(self, district: str, id: int):

        connection = Connection()
        conn = connection.getConnection()

        try:

            query = """UPDATE world.city SET district = %s WHERE id =%s"""
            cursor = conn.cursor()
            up = (district, id)
            cursor.execute(query, up)
            conn.commit()

            print(f'Atualizado com sucesso!')

        except ConnectionError as e:
            print('Failed to Delete: '.format(e))

        finally:

            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')