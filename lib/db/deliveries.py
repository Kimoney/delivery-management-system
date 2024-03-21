from . import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True, nullable=False)
    time = Column(DateTime, default=lambda:datetime.now())
    # Define foreign key relationship with orders table
    order_id = Column(Integer, ForeignKey('orders.id'))
    # Define relationship with Order
    orders = relationship('Order', back_populates='deliveries')
    # Define foreign key relationship with trucks table
    rider_id = Column(Integer, ForeignKey('riders.id'))
    # Define relationship with Rider
    riders = relationship('Rider', back_populates='deliveries')