from . import Base
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    customer_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    # Define relationship with Delivery
    deliveries = relationship("Delivery", back_populates="orders")

if __name__ == '__main__':
    print("<Order Model>")
