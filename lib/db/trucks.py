from .delivery_management_system import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Truck(Base):
    __tablename__ = 'trucks'

    id = Column(Integer, primary_key=True, nullable=False)
    reg_no = Column(String, unique=True, nullable=False)
    truck_capacity = Column(Integer, nullable=False)
    model = Column(String, nullable=False)
    # Define relationship with Rider
    riders = relationship("Rider", back_populates="truck") 