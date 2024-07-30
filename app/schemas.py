from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int


class StudentBase(BaseModel):
    age: int
    gender: int
    ethnicity: int
    parental_education: int
    study_time_weekly: int
    absences: int
    tutoring: int
    parental_support: int
    extracurricular: int
    sports: int
    music: int
    volunteering: int


class Student(StudentBase):
    grade_predicted: int
