from server.sql_base.models import User
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def login(_user: User) -> int | None:
    user = dbmanager.execute(
        query="SELECT id FROM user WHERE login = ? AND password = ?",
        args=(_user.login, _user.password)
    )

    return None if not user else int(user[0])

def register(_user: User) -> int:
    new_id = dbmanager.execute(
        query="insert into user(login, password) values(?, ?)",
        args=(_user.login, _user.password)
    )
    return new_id

def get(user_id: int) -> User | None:
    res = dbmanager.execute(
        query='select * from User where id=(?)',
        args=(user_id,)
    )

    return None if not res else User(
        id=res[0],
        login=res[1],
        password=res[2]
    )
def get_all() -> list[User]:
    user_list = dbmanager.execute(query= "select * from user",many=True)
    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                login=user[1],
                password=user[2]
            ))

    return res

def remove(user_id: int) -> None:
    return dbmanager.execute('delete from user where id=(?)', args=(user_id,))

def update(user_id: int, new_data: User) -> None:
    return dbmanager.execute(
        query='update user set (login, password) = (?,?) where id=(?)',
        args=(new_data.login, new_data.password, user_id))

