from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from models import Base


class Procedure(Base):
    __tablename__ = "procedure"
    id = Column(Integer, primary_key=True, nullable=False)
    source_id = Column(String(100), nullable=False, unique=True)
    patient_id = Column(String(100), ForeignKey("patient.source_id",
                                                ondelete="CASCADE"),
                        nullable=False)
    encounter_id = Column(String(100), ForeignKey("encounter.source_id",
                                                  ondelete="CASCADE"))
    procedure_date = Column(Date, nullable=False)
    type_code = Column(String(100), nullable=False)
    type_code_system = Column(String(100), nullable=False)
    patient = relationship("Patient")
    encounter = relationship("Encounter")
