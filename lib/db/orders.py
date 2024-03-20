from base import Base
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

class CreateOrder:
    def  __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        Session =  sessionmaker(bind=self.engine)
        self.session=Session()



if __name__ == '__main__':

    trial = CreateOrder("trial2.db")
    print(f"\033[92m Successfully created the database \033[0m")
