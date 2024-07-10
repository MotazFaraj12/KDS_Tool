from SQLConnectorDP import SQLConnectorDP
import requests
import time
import sys

# Reconfigure stdout to support UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

def fetch_data(connector):
    url = "http://192.168.0.119:5000/api/data"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()  # or response.text, depending on the API response format
            print(data)
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
    connector = SQLConnectorDP()
    connector.connect()
    
    try:
        t = 5  # Set your interval time in seconds
        run_periodically(t, connector)
    finally:
        connector.close()