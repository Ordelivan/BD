import uvicorn
import fastapi
from fastapi.responses import RedirectResponse
from server.router import routers
from server.sql_base.dbmanger import DbManager

app = fastapi.FastAPI()

[app.include_router(router) for router in routers]

@app.router.get('/', include_in_schema=False)
def index() -> RedirectResponse:
    return RedirectResponse('/docs')


if __name__ == '__main__':
    DbManager('server/sql_base/since.db').create_base('server/sql_base/base.sql')

    uvicorn.run("serverStart:app", reload=True, host='127.0.0.1')

