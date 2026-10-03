from pydantic import BaseModel

# TODO : Create Product model with id, name, price, in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

input = { "id": 345, "name": "Mustard", "price": 599.99, "in_stock": False}
Product1 = Product(**input)    
print(Product1)