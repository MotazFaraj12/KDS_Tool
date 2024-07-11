from SQLConnectorDP import SQLConnectorDP
import requests
import time
import sys
from faker import Faker
import pandas as pd

# Reconfigure stdout to support UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

connector = SQLConnectorDP()
faker = Faker()

def process_data(data):
    for i in range(len(data)):
        if data[i]['status'] == 1:
           orderIds = connector.select_orders(data[i]['id'])
           if not orderIds:
            connector.save_order(data[i])
            for product in data[i]['products']:
                product_data = []
                product_data.append(faker.uuid4())
                product_data.append(product['id'])
                connector.save_order_item(product)
            print(f"Data saved: {data[i]['id']}")
           else:
            for i in range(len(orderIds)):
                OrderItemIds = connector.select_order_item(orderIds[i])
                connector.update_order(data[i]['id'], data[i]['data'])
                connector.update_order_item(OrderItemIds[i], data[i]['data'])
            
def fetch_data(connector):
    url = "http://192.168.0.119:5000/api/data"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # or response.text, depending on the API response format
            process_data(data)
            #print(data)
            #connector.save_data(data)  # Save data to the database
        else:
            print(f"Failed to fetch data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def run_periodically(interval, connector):
    while True:
        fetch_data(connector)
        time.sleep(interval)

if __name__ == "__main__":
    connector.connect()
    try:
        t = 5  # Set your interval time in seconds
        run_periodically(t, connector)
    finally:
        connector.close()