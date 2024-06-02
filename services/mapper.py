from domain.ticket import Ticket


def map_ticket(data: list):
    tickets = []
    for row in data:
        ticket = Ticket(row[0] , row[1] , row[2] , row[3])
        tickets.append(ticket)
    return tickets