import psycopg2

class Dbconnection:
    def execute_query(self, query: str):
        conn = psycopg2.connect(
            dbname="season_tickets",
            user="postgres",
            password="pass123",
            host="localhost",
            port="5432"
        )
        curr = conn.cursor()
        curr.execute(query)
        conn.commit()
        return curr, conn

    def fetch_data(self, query: str):
        conn = psycopg2.connect(
            dbname="season_tickets",
            user="postgres",
            password="pass123",
            host="localhost",
            port="5432"
        )
        curr = conn.cursor()
        curr.execute(query)
        results = curr.fetchall()
        conn.close()
        return results
