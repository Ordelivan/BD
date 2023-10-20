from fastapi import APIRouter
from server.sql_base.models import ticket
from server.resolvers import Ticket


router = APIRouter(prefix='/ticket', tags=['ticket'])

@router.post('/create')
def create(_ticket: ticket) -> int:
    new_id = Ticket.create(_ticket)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{Ticket_id}')
def get(Ticket_id: int) -> ticket | None:
    return Ticket.get(Ticket_id)

@router.get('/')
def get_all() -> list[ticket] | None:
    return Ticket.get_all()

@router.get('/remove/{Ticket_id}')
def remove(Ticket_id: int) -> None:
    return Ticket.remove(Ticket_id)


@router.put("/update/{Ticket_id}")
def update(Ticket_id: int, new_data: ticket):
    return Ticket.update(Ticket_id=Ticket_id, new_data=new_data)