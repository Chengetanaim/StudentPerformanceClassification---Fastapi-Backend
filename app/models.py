from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, Boolean, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, nullable=False, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, nullable=False, primary_key=True)
    age = Column(Integer, nullable=False)
    gender = Column(Integer, nullable=False)
    ethnicity = Column(Integer, nullable=False)
    parental_education = Column(Integer, nullable=False)
    study_time_weekly = Column(Integer, nullable=False)
    absences = Column(Integer, nullable=False)
    tutoring = Column(Integer, nullable=False)
    parental_support = Column(Integer, nullable=False)
    extracurricular = Column(Integer, nullable=False)
    sports = Column(Integer, nullable=False)
    music = Column(Integer, nullable=False)
    volunteering = Column(Integer, nullable=False)
    grade_predicted = Column(Integer, nullable=False)
