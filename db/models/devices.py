from sqlalchemy import Column, Integer, String, Boolean,Date, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Device(Base):
    __tablename__ = "device"
    id = Column(Integer,primary_key = True, index=True)
    company = Column(String,nullable=False)
    company_url = Column(String)
    make = Column(String)
    model = Column(String)
    device_type = Column(String)
    mri = Column(Boolean)
    hazard = Column(Boolean)
    created_at = Column(Date)
    created_by = relationship("User", back_populates="device")
    updated_at = Column(Date)
    updated_by = relationship("User", back_populates="device")

    def __repr__(self):
        return f"device = {self.id}, company = {self.company}"
