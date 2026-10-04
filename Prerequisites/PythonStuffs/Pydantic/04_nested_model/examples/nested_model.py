# A nested model is when you have Pydantic models that contain other Pydantic models as fields.
# This allows you to create complex, hierarchical data structures with proper validation at each level.

from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild() # When you have self referencing object then you must use model.rebuild() 
# well this is optional but recommended beacause sometimes it may fail because in self refernccing
# case models do not refere to models created later or early but themselves
address = Address(
    street = "123 Something",
    city = "Ranchi",
    postal_code = "835222"
)

user1 = User(
    id = 453,
    name = "Ravinandan",
    address = address
)

comment = Comment(
    id = 45,
    content = "beautiful content Man!",
    replies = [
        Comment( id = 2, content = "well said"),
        Comment(id = 5, content = "Where are you from?")
    ]
)

print(comment) # id=45 content='beautiful content Man!' replies=[Comment(id=2, content='well said', replies=None), Comment(id=5, content='Where are you from?', replies=None)]
