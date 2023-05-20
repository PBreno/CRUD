from src.public.DAO.Connection import Connection


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

            for row in records:
                print('-------------------------------------------')
                print(f'ID - {row[0]} | '
                      f'Name - {row[1]} |'
                      f'CountryCode - {row[2]} |'
                      f'District - {row[3]} |'
                      f'Population - {row[4]} \n')

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

            for row in records:
                print('-------------------------------------------')
                print(f'ID - {row[0]} | '
                      f'Name - {row[1]} |'
                      f'CountryCode - {row[2]} |'
                      f'District - {row[3]} |'
                      f'Population - {row[4]} \n')

        except ConnectionError as e:
            print(e)

        finally:
            if conn.is_connected():
                conn.close()
                # cursor.close()
                print('MySQL connection is closed')
