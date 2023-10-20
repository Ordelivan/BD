from fastapi import APIRouter
from server.sql_base.models import Personal
from server.resolvers import personal

router = APIRouter(prefix='/Personal', tags=['Personal'])

@router.post('/login')
def login(_a: Personal) -> Personal | None:
    return personal.login(_a)

@router.post('/register')
def register(_personal: Personal) -> int:
    new_id = personal.register(_personal)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{personal_id}')
def get(personal_id: int) -> Personal | None:
    return personal.get(personal_id)

@router.get('/')
def get_all() -> list[Personal] | None:
    return personal.get_all()

@router.get('/remove/{personal_id}')
def remove(personal_id: int) -> None:
    return personal.remove(personal_id)


@router.put("/update/{personal_id}")
def update(personal_id: int, new_data: Personal):
    return personal.update(personal_id=personal_id, new_data=new_data)

