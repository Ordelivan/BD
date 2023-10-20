from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class theatre_type(BaseModelModify):
    name: str

    class theatre(BaseModelModify):
    locationid: int
    name: str
    typeid: int

class location(BaseModelModify):
    adress: str
    countryid: int

    class country(BaseModelModify):
    name: str

    class performance(BaseModelModify):
    name: str
    performance_date: str
    presonalId: int
    theatreid: int
    genreid: int

    class genre(BaseModelModify):
    name: str


class User(BaseModelModify):
    login: str
    password: str

class Personal(User):
    login: str
    password: str
    jobid: int

class jobs(BaseModelModify):
    name: str

class tickets(BaseModelModify):
    userid: int
    performanceid: int




