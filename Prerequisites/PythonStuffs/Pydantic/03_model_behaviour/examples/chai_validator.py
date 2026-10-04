from pydantic import BaseModel, field_validator,model_validator, computed_field 

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v): # v ke andar username aa jayega
        if len(v) < 4:
            raise ValueError ("Username must be atleast 4 character")
        return v

class SignUp(BaseModel):
    password: str
    confirm: str

    @model_validator(mode = 'after')
    def password_match(cls,value):
        if value.password != value.confirm:
            raise ValueError("Password entered do not match")
        return value

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

