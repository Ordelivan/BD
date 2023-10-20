from server.sql_base.models import ticket
from server.sql_base.dbmanger import DbManager

dbmanager = DbManager(base_path='server/sql_base/since.db')

def create(_ticket: ticket) -> int:
    new_id = dbmanager.execute(
        query="insert into ticket(userid,performanceid) values(?,?)",
        args=(_ticket.userid,_ticket.performanceid)
    )
    return new_id

def get(ticket_id: int) -> ticket | None:
    res = dbmanager.execute(
        query='select * from ticket where id=(?)',
        args=(ticket_id,)
    )

    return None if not res else ticket(
        id=res[0],
        userid=res[1],
        performanceid=res[2],

    )
def get_all() -> list[ticket]:
    ticket_list = dbmanager.execute(query="select * from ticket", many=True)
    res = []

    if ticket_list:
        for _ticket in ticket_list:
            res.append(ticket(
                id=_ticket[0],
                userid=_ticket[1],
                performanceid=_ticket[2],


            ))

    return res

def remove(ticket_id: int) -> None:
    return dbmanager.execute('delete from ticket where id=(?)', args=(ticket_id,))

def update(ticket_id: int, new_data: ticket) -> None:
    return dbmanager.execute(
        query='update ticket set (userid,performanceid) = (?,?) where id=(?)',
        args=(new_data.userid,new_data.performanceid))