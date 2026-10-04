# Serialization is converting the Pydantic object into a format that’s easier to store or
# send—here, a Python dictionary with model_dump() or a JSON string with model_dump_json().
from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict( # just to show how to use json_encoders in pydantic v2
        json_encoders = { datetime: lambda v : v.strftime('%d-%m-%Y %H:%M:%S')
                            }
    )


# Create a user instance

user1 = User(
    id = 34,
    name = "Ravinandan Singh",
    email = "ornsamrat2004@gmail.com",
    is_active = True,
    created_at = datetime(2026, 10, 4),
    address = Address(
        street = "Asha Colony",
        city = "Gaya",
        zip_code = "824908" 
    ),
    tags = ["premium", "subscribe"]

)

# Using model_dump() -> dict
python_dict = user1.model_dump()
print(f"Dump: \n{python_dict}")

# Using model_dump_json() -> json

user_json = user1.model_dump_json()
print(f"JSON: \n{user_json}")