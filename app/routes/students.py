from fastapi import APIRouter, HTTPException, status, Depends
from .. import database, models, schemas, utils, oauth2
from sqlalchemy.orm import Session
import pickle

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Student)
def predict_grade(
    student: schemas.StudentBase,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    grade_predicted = model.predict([list(student.model_dump().values())])

    print(int(grade_predicted[0]))
    db_student = models.Student(
        **student.model_dump(), grade_predicted=int(grade_predicted[0])
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@router.get("/", response_model=list[schemas.Student])
def get_predicted_students(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    student = db.query(models.Student).all()
    return student
