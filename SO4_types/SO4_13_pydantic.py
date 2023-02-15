from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id : int
    name = "Emiliano La Mata"
    signup_ts : datetime | None = None
    friends : list[int]

# Desde el exterior podríamos recibir estos datos:
external_data = {
    'id' : 1001,
    'signup_ts' : "2002-10-23 12:00",
    'friends' : [1001, 1002, 1003]
}

user = User(**external_data)
print(user)
print(user.id)