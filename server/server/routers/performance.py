from fastapi import APIRouter
from server.sql_base.models import performance
from server.resolvers import Performance


router = APIRouter(prefix='/performance', tags=['performance'])

@router.post('/create')
def create(_performance: performance) -> int:
    new_id = Performance.create(_performance)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{Performance_id}')
def get(Performance_id: int) -> performance | None:
    return Performance.get(Performance_id)

@router.get('/')
def get_all() -> list[performance] | None:
    return Performance.get_all()

@router.get('/remove/{Performance_id}')
def remove(Performance_id: int) -> None:
    return Performance.remove(Performance_id)


@router.put("/update/{Performance_id}")
def update(Performance_id: int, new_data: performance):
    return Performance.update(Performance_id=Performance_id, new_data=new_data)