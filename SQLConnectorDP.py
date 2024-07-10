import json
import pyodbc
import os
import sys

class SQLConnectorDP:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self):
        if getattr(sys, 'frozen', False):
            script_dir = os.path.dirname(sys.executable)
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        config_path = os.path.join(script_dir, 'config.json')

        try:
            with open(config_path) as f:
                config = json.load(f)
        except FileNotFoundError:
            print(f"Configuration file not found at {config_path}")
            return
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the configuration file at {config_path}")
            return

        server = config.get('server')
        database = config.get('database')
        username = config.get('username')
        password = config.get('password')

        if not all([server, database, username, password]):
            print("Database configuration is missing required fields")
            return

        connection_string = f'Driver={{SQL Server}};Server={server};Database={database};UID={username};PWD={password};'

        try:
            self.connection = pyodbc.connect(connection_string, autocommit=True)
            self.cursor = self.connection.cursor()
            print("Connection successful!")
        except pyodbc.Error as ex:
            print(f"Error: {str(ex)}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


