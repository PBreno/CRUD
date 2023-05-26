import mysql.connector

from src.public.DAO.Connection import Connection
from tabulate import tabulate


class WorldDAO:

    def __init__(self, connection):
        self.connection = Connection().getConnection()

    def selectCity(self):

        try:

            query = """SELECT *FROM world.city;"""
            cursor = self.connection.cursor()
            cursor.execute(query)

            records = cursor.fetchall()
            print(f'Total number of rows in table: {cursor.rowcount}')

            print(tabulate(records, headers=['ID', 'Name', 'CountryCode', 'District', 'Population'],
                           tablefmt='fancy_grid'))

        except ConnectionError as e:
            print(e)

        finally:
            if self.connection.is_connected():
                self.connection.close()
                # cursor.close()
                print('MySQL connection is closed')

    def selectCityID(self, id: int):

        try:

            query = f'SELECT *FROM world.city WHERE id = {id};'

            cursor = self.connection.cursor()
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
            if self.connection.is_connected():
                self.connection.close()
                # cursor.close()
                print('MySQL connection is closed')

    def createCity(self, name: str, country_code: str, district: str, population: int):

        try:

            query = """INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"""

            records = (name, country_code, district, population)
            cursor = self.connection.cursor()
            cursor.execute(query, records)
            self.connection.commit()

            print(f'Dados inseridos: {records}')

        except ConnectionError as e:
            print(e)

        finally:
            if self.connection.is_connected():
                self.connection.close()
                # cursor.close()
                print('MySQL connection is closed')

    def delete(self, id: int):

        try:

            query = f'DELETE FROM world.city WHERE id = {id}'
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()

            print(f'ID {id} excluido com sucesso!')

        except ConnectionError as e:
            print('Failed to Delete: '.format(e))

        finally:

            if self.connection.is_connected():
                self.connection.close()
                # cursor.close()
                print('MySQL connection is closed')

    def update(self, district: str, id: int):

        try:

            query = """UPDATE world.city SET district = %s WHERE id =%s"""
            cursor = self.connection.cursor()
            up = (district, id)
            cursor.execute(query, up)
            self.connection.commit()

            print(f'Atualizado com sucesso!')

        except ConnectionError as e:
            print('Failed to Delete: '.format(e))

        finally:

            if self.connection.is_connected():
                self.connection.close()
                # cursor.close()
                print('MySQL connection is closed')
