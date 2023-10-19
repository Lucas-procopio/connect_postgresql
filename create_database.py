import psycopg2
import yaml
from yaml.loader import SafeLoader
import os

class Create_database():
    conn = psycopg2.connect(user="postgres", password='"pwd"', host="127.0.0.1", port="5432", database="postgres")
    conn.autocommit = True
    cursor=conn.cursor()
    
    def __init__(self, database=None, user=None, password=None, host=None, port=None, conn=conn, cursor=cursor):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = conn
        self.cursor = cursor

    def _gettingfiles(path='./tables'):
        files = [file for file in os.listdir('./tables')]
        return files

    def _gettingfield(fields):
        print(fields)
        with open(fields) as f:
            data = yaml.load(f, Loader=SafeLoader)
            print(data)
        return data
    
    def create_Table(self):
        tables = self._gettingfiles()
        for table_name in tables:
            table_fields = self._gettingfield(table_name)
            try:
                sql = f'''CREATE TABLE {table_name} {table_fields}'''
                self.cursor.execute(sql)
                print('Table was created!')
                self.conn.close()
            except:
                print(f'Table {table_name} exist!')

if __name__ == '__main__':
    database = Create_database()
    database.create_Table()