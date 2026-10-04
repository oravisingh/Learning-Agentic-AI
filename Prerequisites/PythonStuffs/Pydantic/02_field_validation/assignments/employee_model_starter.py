from pydantic import BaseModel, Field
from typing import Optional
# TODO : Create an Employee Model
# Fields:]]
# -id: int
# -name: str (min 3 char)
# -department: optional str (default "General")
# -salary: float (must be >= 10000)

class Employee(BaseModel): 
    id: int
    name: str = Field(
        ...,
        min_length = 3,
        max_length = 20,
        description = "Employee Name",
        example = "Ravinandan Samrat",
        ) # type: ignore
    department: Optional[str]= 'General'
    salary: float = Field(
        ...,
        ge = 10000
        )

input ={"id":124, "name":"Ravinandan", "department": "Finance", "salary": 15000}

emp1 = Employee(**input)
print(emp1)
