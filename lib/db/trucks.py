from base import Base
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import sessionmaker, relationship

class Truck(Base):
    __tablename__ = 'trucks'

    id = Column(Integer, primary_key=True, nullable=False)
    reg_no = Column(String, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)