from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes import users, auth, students

app = FastAPI(
    title="Student Performance Classification",
    description="Classifying a student's final grade using attributes such as their ethnicity, age and weekly study time.",
)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {"message": "Hello, world!"}


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(students.router)
