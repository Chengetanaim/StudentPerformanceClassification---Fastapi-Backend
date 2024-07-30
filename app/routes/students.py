from fastapi import APIRouter, HTTPException, status, Depends
from .. import database, models, schemas, utils
from sqlalchemy.orm import Session
import pickle

router = APIRouter(prefix="/students", tags=["Students"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def predict_grade(student: schemas.StudentBase, db: Session = Depends(database.get_db)):
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    grade_predicted = model.predict([list(student.model_dump().values())])
    print(grade_predicted)
    return {"message": "Model successfully loaded in."}
