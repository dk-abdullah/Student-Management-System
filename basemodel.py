from pydantic import BaseModel,Field
from typing import Annotated,Literal,Optional

class Student(BaseModel):
    id : Annotated[str, Field(..., description = "Id of the Student", example = "s001")]
    Name: Annotated[str,Field(...,description ="Name of the Student")]
    age: Annotated[int ,Field(...,description = "Age of the Student")]
    roll_no: Annotated[str,Field(...,description = "Roll no of the student")]
    Department : Annotated[str,Field(..., description = "Department of the Student")]
    Semester : Annotated[str,Field(..., description = "Semester of the Student")]
    Section : Annotated[str,Field(...,description = "Section of the Student")]
    Badge : Annotated[str,Field(...,description = "Badge of the Student", example = "FA24")]
    Gender : Annotated[Literal['male','female'], Field(..., description = "Gender of the Student")]
    City : Annotated[str, Field(..., description = "City of the Student")]


class Update_Student(BaseModel):
    Name :Annotated[Optional[str], Field(default = None)]
    age : Annotated[Optional[int], Field(default = None)]
    roll_no : Annotated[Optional[str], Field(default = None)]
    Department : Annotated[Optional[str], Field(default = None)]
    Semester : Annotated[Optional[str], Field(default = None)]
    Section : Annotated[Optional[str], Field(default = None)]
    Badge : Annotated[Optional[str], Field(default = None)]
    Gender : Annotated[Optional[Literal['male','female']], Field(default = None)]
    City : Annotated[Optional[str], Field(default = None)]