import psycopg2

class DAO:
    conn_string = ""

    def create_connection(self):
        return psycopg2.connect(self.conn_string)