from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship

from models import Base


class Observation(Base):
    __tablename__ = "observation"
    id = Column(Integer, primary_key=True, nullable=False)
    source_id = Column(String(100), nullable=False)
    patient_id = Column(String(100), ForeignKey("patient.source_id",
                                                ondelete="CASCADE"),
                        nullable=False)
    encounter_id = Column(String(100), ForeignKey("encounter.source_id",
                                                  ondelete="CASCADE"))
    observation_date = Column(Date, nullable=False)
    type_code = Column(String(100), nullable=False)
    type_code_system = Column(String(100), nullable=False)
    value = Column(DECIMAL, nullable=False)
    unit_code = Column(String(100))
    unit_code_system = Column(String(100))
    patient = relationship("Patient")
    encounter = relationship("Encounter")
