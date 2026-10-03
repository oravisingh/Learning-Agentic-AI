from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User(name="Asha", age="25")

print(user)
print(user.age, type(user.age))