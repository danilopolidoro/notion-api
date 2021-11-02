'''Define the user object for Notion'''

from pydantic import BaseModel
from enum import Enum


class Types(str, Enum):
    person = "person"
    bot = "bot"

class Person(BaseModel):
    email:str

class User(BaseModel):
    object: str = "user"
    id: str
    type:Types = Types.person
    name:str = None
    avatar_url:str = None
    person:Person=None
