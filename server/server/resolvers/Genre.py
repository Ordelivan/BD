from server.sql_base.models import genre
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def create(_genre: genre) -> int:
    new_id = dbmanager.execute(
        query="insert into genre(name) values(?)",
        args=(_genre.name)
    )
    return new_id

def get(genre_id: int) -> genre | None:
    res = dbmanager.execute(
        query='select * from genre where id=(?)',
        args=(genre_id,)
    )

    return None if not res else genre(
        id=res[0],
        name=res[1]
    )
def get_all() -> list[genre]:
    genre_list = dbmanager.execute(query="select * from genre", many=True)
    res = []

    if genre_list:
        for _genre in genre_list:
            res.append(genre(
                id=_genre[0],
                name=_genre[1]
            ))

    return res

def remove(сonference_id: int) -> None:
    return dbmanager.execute('delete from genre where id=(?)', args=(сonference_id,))

def update(сonference_id: int, new_data: genre) -> None:
    return dbmanager.execute(
        query='update genre set (name) = (?) where id=(?)',
        args=(new_data.name,сonference_id))
