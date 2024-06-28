from pydantic import BaseModel
from enum import Enum

class Role(str, Enum):
    ADMIN = "Admin"
    USER = "User"
    ANALYTICS ="Analytics"

class User(BaseModel):
    id: str
    name: str
    roles: Role