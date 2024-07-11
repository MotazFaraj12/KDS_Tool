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
    
    def select_orders(self , id):
        self.cursor.execute("SELECT order_id, table_id,order_status,order_time,completion_time,order_source, order_number FROM dbo.Orders WHERE order_id = ?", (id,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def select_order_item(self , id):
        self.cursor.execute("SELECT order_item_id,menu_item_id,special_instruction,status,prep_start_time,prep_end_time,prep_time,modifiers,LastScreen,OnTimeStatus, order_id FROM dbo.OrderMenuItem WHERE order_id = ?", (id,))
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]    
      
    def update_order(self, id, new_data):
        self.cursor.execute("UPDATE dbo.Orders SET data = ? WHERE order_id = ?", (new_data, id))
        self.connection.commit()
    
    def update_order_item(self, id, new_data):
        self.cursor.execute("UPDATE dbo.Orders SET data = ? WHERE order_id = ?", (new_data, id))
        self.connection.commit()
    
    def save_order(self, data):
        self.cursor.execute("INSERT INTO Order (order_id,table_id,order_status,order_time,completion_time,order_source, order_number) VALUES (?,?,?,?,?,?,?)", (data['id'], data['table_id'], data['status'], data['order_time'], data['completion_time'], data['order_source'], data['order_number']))
        self.connection.commit()

    def save_order_item(self, data):
        for key, value in data.items():
            self.cursor.execute("INSERT INTO OrderMenuItem (order_item_id,menu_item_id,special_instruction,status,prep_start_time,prep_end_time,prep_time,modifiers,LastScreen,OnTimeStatus, order_id) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (value['order_item_id'], value['menu_item_id'], value['special_instruction'], value['status'], value['prep_start_time'], value['prep_end_time'], value['prep_time'], value['modifiers'], value['LastScreen'], value['OnTimeStatus'], value['order_id']))
        self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


