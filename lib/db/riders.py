from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Rider(Base):
    __tablename__ = 'riders'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    location = Column(String, unique=True, nullable=False)
    # Define foreign key relationship with trucks table
    truck_id = Column(Integer, ForeignKey('trucks.id'))
    # Define relationship with Truck
    truck = relationship('Truck', back_populates='riders')
    # Define relationship with Delivery
    deliveries = relationship("Delivery", back_populates="riders")