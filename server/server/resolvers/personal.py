from server.sql_base.models import Personal
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def login(_personal: Personal) -> int | None:
    Personal = dbmanager.execute(
        query="SELECT id FROM Personal WHERE login = ? AND password = ?",
        args=(_personal.login, _personal.password)
    )

    return None if not Personal else int(Personal[0])

def register(_personal: Personal) -> int:
    new_id = dbmanager.execute(
        query="insert into Personal(login, password, power_level) values(?, ?, ?)",
        args=(_personal.login, _personal.password, _personal.power_level)
    )
    return new_id

def get(personal_id: int) -> Personal | None:
    res = dbmanager.execute(
        query='select * from Personal where id=(?)',
        args=(personal_id,)
    )

    return None if not res else Personal(
        id=res[0],
        login=res[1],
        password=res[2],
        power_level=res[3]
    )
def get_all() -> list[Personal]:
    personal_list = dbmanager.execute(query= "select * from Personal", many=True)
    res = []

    if personal_list:
        for personal in personal_list:
            res.append(Personal(
                id=personal[0],
                login=personal[1],
                password=personal[2],
                power_level=personal[3]
            ))

    return res

def remove(personal_id: int) -> None:
    return dbmanager.execute('delete from Personal where id=(?)', args=(personal_id,))

def update(personal_id: int, new_data: Personal) -> None:
    return dbmanager.execute(
        query='update Personal set (login, password, power_level) = (?, ?, ?) where id=(?)',
        args=(new_data.login, new_data.password, new_data.power_level,personal_id))

