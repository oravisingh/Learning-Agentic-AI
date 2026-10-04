from pydantic import BaseModel
from typing import List, Optional

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons


class Lesson(BaseModel):
    lesson_id : int
    name : str
    content : str

class Module(BaseModel):
    module_id : int
    name : str
    content : str
    lesson : List[Lesson]

class Course(BaseModel):
    name : str
    price : float
    module : List[Module]

# This created a hierarchy: Course → Modules → Lessons

# We are not usimg the model.rebuild since we are not doing here any forward refrencing to SELF and normal referncing can be taken care by pydantic easily
