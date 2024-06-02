from domain.ticket import Ticket
from Connection.repoTicket import RepositoryTicket
from services.mapper import map_ticket
from fastapi import HTTPException


class TicketServices:
    repo_ticket = RepositoryTicket()

    def get_tickets(self):
        return map_ticket(self.repo_ticket.get_tickets())

    def get_ticket(self, id: int):
        list_ticket = map_ticket(self.repo_ticket.get_ticket(id))
        if not list_ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return list_ticket[0]

    def get_ticket_by_name(self, name: str):
        tickets = map_ticket(self.repo_ticket.get_ticket_by_name(name))
        if not tickets:
            raise HTTPException(status_code=404, detail="Ticket not found")
        return tickets[0]

    def create_ticket(self, ticket: Ticket):
        new_ticket_id = self.repo_ticket.create_ticket(ticket)
        created_ticket = self.repo_ticket.get_ticket(new_ticket_id)
        return {"message": "Παναθηναϊκός: Το εισιτήριο δημιουργήθηκε επιτυχώς", "ticket": map_ticket(created_ticket)}

    def update_ticket_by_name(self, ticket: Ticket):
        self.repo_ticket.update_ticket_by_name(ticket)
        updated_ticket = self.get_ticket_by_name(ticket.name)
        return {"message": "Παναθηναϊκός: Το εισιτήριο ενημερώθηκε επιτυχώς", "ticket": updated_ticket}

    def delete_ticket_by_name(self, name: str):
        if not self.repo_ticket.get_ticket_by_name(name):
            raise HTTPException(status_code=404, detail="Ticket not found")
        self.repo_ticket.delete_ticket_by_name(name)
        return {"message": "Παναθηναϊκός: Το εισιτήριο διαγράφηκε επιτυχώς"}

    def search_tickets(self, name: str = None):
        return map_ticket(self.repo_ticket.search_tickets(name))

    def update_stock_by_name(self, name: str, quantity: int):
        if not self.repo_ticket.get_ticket_by_name(name):
            raise HTTPException(status_code=404, detail="Ticket not found")
        self.repo_ticket.update_stock_by_name(name, quantity)
        return {"message": "Παναθηναϊκός: Το απόθεμα ενημερώθηκε επιτυχώς"}

    def get_statistics(self):
        stats = self.repo_ticket.get_statistics()
        return {
            "total_products": stats[0],
            "average_price": stats[1],
            "total_quantity": stats[2]
        }

    def get_ticket_nearly_sold_out(self):
        return map_ticket(self.repo_ticket.get_ticket_nearly_sold_out())
