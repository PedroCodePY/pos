from fastapi import FastAPI, Path

app = FastAPI()

students={
    "S1001":{
        "name":"Alice",
        "age":20,
        "major":"Computer Science",
        "gpa":3.8,
        "courses":["CS101","CS102","MATH101"],
        "Status":"Active",
        "StudentID":"S1001"
    }
}

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/student/{student_id}")
def get_student(student_id: str = Path(None,description="The ID of the student to retrieve")):
    return students[student_id]