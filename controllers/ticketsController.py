from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from services.ticketServices import TicketServices
from domain.ticket import Ticket

router = APIRouter()

class TicketCreateUpdate(BaseModel):
    name: str
    price: float
    quantity: int

class StockUpdate(BaseModel):
    quantity: int

@router.get('/all')
async def get_tickets():
    service = TicketServices()
    return service.get_tickets()

@router.get('/ticket/{name}')
async def get_ticket(name: str):
    service = TicketServices()
    return service.get_ticket_by_name(name)

@router.post('/create')
async def create_ticket(ticket: TicketCreateUpdate):
    service = TicketServices()
    new_ticket = Ticket(id=0, name=ticket.name, price=ticket.price, quantity=ticket.quantity)
    return service.create_ticket(new_ticket)

@router.put('/update/{name}')
async def update_ticket(name: str, ticket: TicketCreateUpdate):
    service = TicketServices()
    updated_ticket = Ticket(id=0, name=name, price=ticket.price, quantity=ticket.quantity)
    return service.update_ticket_by_name(updated_ticket)

@router.delete('/delete/{name}')
async def delete_ticket(name: str):
    service = TicketServices()
    return service.delete_ticket_by_name(name)

@router.get('/search/')
async def search_tickets(name: str = Query(None)):
    service = TicketServices()
    return service.search_tickets(name)

@router.put('/stock/{name}')
async def update_stock(name: str, stock_update: StockUpdate):
    service = TicketServices()
    return service.update_stock_by_name(name, stock_update.quantity)

@router.get('/statistics/')
async def get_statistics():
    service = TicketServices()
    return service.get_statistics()

@router.get('/soldOut')
async def get_ticket_nearly_sold_out():
    service = TicketServices()
    return service.get_ticket_nearly_sold_out()
