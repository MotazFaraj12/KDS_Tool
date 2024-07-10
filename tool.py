from SQLConnectorDP import SQLConnectorDP

if __name__ == "__main__":
    connector = SQLConnectorDP()
    connector.connect()
    # Do some database operations
    connector.close()
