from fastapi import APIRouter
from server.sql_base.models import genre
from server.resolvers import Genre


router = APIRouter(prefix='/genre', tags=['genre'])

@router.post('/create')
def create(_genre: genre) -> int:
    new_id = Genre.create(_genre)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{Genre_id}')
def get(Genre_id: int) -> genre | None:
    return Genre.get(Genre_id)

@router.get('/')
def get_all() -> list[genre] | None:
    return Genre.get_all()

@router.get('/remove/{Genre_id}')
def remove(Genre_id: int) -> None:
    return Genre.remove(Genre_id)


@router.put("/update/{Genre_id}")
def update(Genre_id: int, new_data: genre):
    return Genre.update(Genre_id=Genre_id, new_data=new_data)

