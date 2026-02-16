from fastapi import FastAPI,Path,HTTPException,Query
import json
from fastapi.responses import JSONResponse 
from basemodel import Student,Update_Student

app = FastAPI()


def load_data():
    with open("Students.json", "r") as f:
        data =json.load(f)
    
    return data

def save_data(data):
    with open("Students.json", "w") as f:
        json.dump(data,f)
# For check
@app.get("/")
def intro():
    return {"message":"Student Management System"}
# To check the list of students
@app.get("/view")
def view():
    data = load_data()

    return data
# To check students through their id
@app.get("/Student/{student_id}")
def view_student(student_id: str = Path(..., description = "Id of the student from the Data Base", example = "s001")):
    data = load_data()

    if student_id in data:
        return data[student_id]
    raise HTTPException(status_code=404, detail="Patient not found")
# To sort students
@app.get("/sort")
def sort(sort_by : str = Query(..., description="Sort on the basis of Semester , Sections"), order :str = Query('asc', description = "Sort in Ascending or Descending order")):
    valid_fields = ['Semester','Section']
    valid_order = ['asc','desc']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail =f"invalid fileds kindly select from{valid_fields}")
    
    if order not in valid_order:
        raise HTTPException(status_code=400, detail="Kindly select between asc and desc")
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by,0), reverse=sort_order)
    return sorted_data
# Create new Student
@app.post("/create")
def create_student(student:Student):
    data = load_data()

    if student.id in data:
        raise HTTPException(status_code= 400, detail="Student Already Exists")
    
    data[student.id] = student.model_dump(exclude =['id'])

    save_data(data)

    return JSONResponse(status_code=201, content={"message":"Student created Successfully"})

# Update Student
@app.put("/edit/{student_id}")
def update_student(student_id : str, student_update:Update_Student):
    data = load_data()

    if student_id not in data:
        raise HTTPException(status_code= 404, detail="Student not found")
    
    existing_student_info= data[student_id]
    updated_student_info = student_update.model_dump(exclude_unset = True)

    for key,value in updated_student_info.items():
        existing_student_info[key] = value

    existing_student_info['id'] = student_id
    student_pydantic_obj = Student(**existing_student_info)

    existing_student_info = student_pydantic_obj.model_dump(exclude =['id'])

    data[student_id] = existing_student_info

    save_data(data)
    return JSONResponse(status_code= 200, content={"message":"Student Updated Successfully"})


@app.delete('/delete/{student_id}')
def delete_student(student_id : str):
    # load data
    data = load_data()
    
    if student_id not in data:
        raise HTTPException(status_code= 404, detail = "Student not found")
    
    del data[student_id]
    
    save_data(data)
    return JSONResponse(status_code= 200, content = "Student deleted")