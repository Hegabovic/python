import mysql.connector


class DatabaseConnector:
    is_connected = False

    def __init__(self, host, database_name, username, password):
        self.localhost = host
        self.database_name = database_name
        self.username = username
        self.password = password

    def establish_connection(self):
        try:
            connection = mysql.connector.connect(host=self.localhost,
                                                 database=self.database_name,
                                                 user=self.username,
                                                 password=self.password)
            DatabaseConnector.is_connected = True
            print('connection has established')
            return connection

        except mysql.connector.Error as error:
            print("Failed to connect MySQL: {}".format(error))

    @staticmethod
    def close_connection(cursor, connection):
        if DatabaseConnector.is_connected:
            cursor.close()
            connection.close()
            print('MySQL connection is closed')
