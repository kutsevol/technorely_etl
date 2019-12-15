from sqlalchemy import Column, Integer, String, Date

from models import Base


class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True, nullable=False)
    source_id = Column(String(100), nullable=False, unique=True)
    birth_date = Column(Date)
    gender = Column(String(100))
    race_code = Column(String(100))
    race_code_system = Column(String(100))
    ethnicity_code = Column(String(100))
    ethnicity_code_system = Column(String(100))
    country = Column(String(100))
