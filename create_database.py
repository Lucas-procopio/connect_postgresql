import psycopg2
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

    def create_database(self, database_name):
        sql = f'''CREATE database {database_name}'''
        self.cursor.execute(sql)
        print('Database has been created successfully!')
        self.conn.close()

    def create_Table(self, table_name):#, campos:list, tipo_campos:list):
        sql = f'''CREATE TABLE {table_name} (nome varchar);'''
        self.cursor.execute(sql)
        print('Table was created!')
        self.conn.close()