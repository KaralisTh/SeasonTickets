from domain.ticket import Ticket
from Connection.connector import Dbconnection

class RepositoryTicket:
    repositoryPostgres = Dbconnection()

    def get_ticket(self, ident: int):
        query = f"SELECT * FROM season_tickets WHERE id = {ident}"
        return self.repositoryPostgres.fetch_data(query)

    def get_ticket_by_name(self, name: str):
        query = f"SELECT * FROM season_tickets WHERE name = '{name}'"
        return self.repositoryPostgres.fetch_data(query)

    def get_tickets(self):
        query = "SELECT * FROM season_tickets"
        return self.repositoryPostgres.fetch_data(query)

    def create_ticket(self, ticket: Ticket):
        query = f"""
        INSERT INTO season_tickets (name, price, quantity) VALUES 
        ('{ticket.name}', {ticket.price}, {ticket.quantity})
        RETURNING id
        """
        curr, conn = self.repositoryPostgres.execute_query(query)
        new_ticket_id = curr.fetchone()[0]
        conn.close()
        return new_ticket_id

    def update_ticket_by_name(self, ticket: Ticket):
        query = f"""
        UPDATE season_tickets SET price = {ticket.price}, quantity = {ticket.quantity}
        WHERE name = '{ticket.name}'
        """
        curr, conn = self.repositoryPostgres.execute_query(query)
        conn.close()
        return True

    def delete_ticket_by_name(self, name: str):
        query = f"DELETE FROM season_tickets WHERE name = '{name}'"
        curr, conn = self.repositoryPostgres.execute_query(query)
        conn.close()
        return True

    def search_tickets(self, name: str = None):
        query = "SELECT * FROM season_tickets WHERE 1=1"
        if name:
            query += f" AND name ILIKE '%{name}%'"

        return self.repositoryPostgres.fetch_data(query)

    def update_stock_by_name(self, name: str, quantity: int):
        query = f"UPDATE season_tickets SET quantity = quantity + {quantity} WHERE name = '{name}'"
        curr, conn = self.repositoryPostgres.execute_query(query)
        conn.close()
        return True

    def get_statistics(self):
        query = """
        SELECT COUNT(*), AVG(price), SUM(quantity) FROM season_tickets
        """
        return self.repositoryPostgres.fetch_data(query)[0]

    def get_ticket_nearly_sold_out(self):
        query = "SELECT * FROM season_tickets WHERE quantity <=50 "
        return self.repositoryPostgres.fetch_data(query)
