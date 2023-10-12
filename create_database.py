import psycopg2
import os

class Create_database():
    conn = psycopg2.connect(
        database="postgres",
        user='postgres',
        password= 'pwd', #os.environ['password'],
        host='localhost',
        port='5432' #os.environ['port']
    )    
    conn.autocommit = True
    cursor = conn.cursor() # Creating coursor object

    def __init__(self, database=None, user=None, password=None, host=None, port=None, conn=None, cursor=None):
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