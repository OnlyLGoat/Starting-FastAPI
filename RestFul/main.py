# Import FastAPI and BaseModel
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel

# Create Our App
app = FastAPI()

# Our Student Class With Pydantic
class Student(BaseModel):
    id: int
    name: str
    grade: int
    
# Create Our Students List
Students = [
    Student(id= 1, name= 'Amine', grade= 12),
    Student(id= 2, name= 'Ali', grade= 17)
]

# Read Our Students
@app.get('/students')
def read_students():
    return Students

# Create A Student
@app.post('/students')
def create_student(new_student: Student):
    Students.append(new_student)
    return new_student

# Update A Student
@app.put("/students/{sdt_id}")
def update_student(sdt_id: int, updated_student: Student):
    for index, student in enumerate(Students):
        if student.id == sdt_id:
            Students[index] = updated_student
            return updated_student
    raise HTTPException(status_code=404, detail="Student not found")

# Delete A Student
@app.delete("/students/{sdt_id}")
def delete_student(sdt_id: int):
    for index, student in enumerate(Students):
        if student.id == sdt_id:
            del Students[index]
            return { "message": "Student Was Deleted !" }
    raise HTTPException(status_code=404, detail="Student not found")