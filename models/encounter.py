from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from models import Base


class Encounter(Base):
    __tablename__ = "encounter"
    id = Column(Integer, primary_key=True, nullable=False)
    source_id = Column(String(100), nullable=False, unique=True)
    patient_id = Column(String(100), ForeignKey("patient.source_id",
                                                ondelete="CASCADE"),
                        nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    type_code = Column(String(100))
    type_code_system = Column(String(100))
    patient = relationship("Patient")
