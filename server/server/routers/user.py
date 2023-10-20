from fastapi import APIRouter
from server.sql_base.models import User
from server.resolvers import user

router = APIRouter(prefix='/user', tags=['User'])

@router.post('/login')
def login(_user: User) -> User | None:
    return user.login(_user)

@router.post('/register')
def register(_user: User) -> int:
    new_id = user.register(_user)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{user_id}')
def get(user_id: int) -> User | None:
    return user.get(user_id)

@router.get('/')
def get_all() -> list[User] | None:
    return user.get_all()

@router.get('/remove/{user_id}')
def remove(user_id: int) -> None:
    return user.remove(user_id)


@router.put("/update/{user_id}")
def update(user_id: int, new_data: User):
    return user.update(user_id=user_id, new_data=new_data)

