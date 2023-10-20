from server.sql_base.models import performance
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def create(_performance: performance) -> int:
    new_id = dbmanager.execute(
        query="insert into performance(name,performance_date,presonalId,theatreid,genreid) values(?,?,?,?,?)",
        args=(_performance.name,_performance.performance_date,_performance.presonalId,_performance.theatreid,_performance.genreid)
    )
    return new_id

def get(performance_id: int) -> performance | None:
    res = dbmanager.execute(
        query='select * from performance where id=(?)',
        args=(performance_id,)
    )

    return None if not res else performance(
        id=res[0],
        name=res[1],
        performance_date=res[2],
        presonalId=res[3],
        theatreid=res[4],
        genreid=res[5]
    )
def get_all() -> list[performance]:
    performance_list = dbmanager.execute(query="select * from performance", many=True)
    res = []

    if performance_list:
        for _performance in performance_list:
            res.append(performance(
                id=_performance[0],
                name=_performance[1],
                performance_date=_performance[2],
                presonalId=_performance[3],
                theatreid=_performance[4],
                genreid=_performance[5]

            ))

    return res

def remove(performance_id: int) -> None:
    return dbmanager.execute('delete from performance where id=(?)', args=(performance_id,))

def update(performance_id: int, new_data: performance) -> None:
    return dbmanager.execute(
        query='update performance set (name,performance_date,presonalId,theatreid,genreid) = (?,?,?,?,?) where id=(?)',
        args=(new_data.name,new_data.performance_date,new_data.presonalId,new_data.theatreid,new_data.genreid,performance_id))
