from pydantic import BaseModel

class User(BaseModel):
   id: int
   name: str
   is_active :bool

input_data = {"id": 244, "name": "Ravinandan", "is_active": True}

user1 = User(**input_data)
print(user1)

# Pydantic also tried to solve the type problem as much it can like
input_data1 = {"id": '244', "name": "Ravinandan", "is_active": "True"}

user2 = User(**input_data1) # type: ignore
print(user2)