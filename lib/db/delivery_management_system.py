
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from . import Base
from .orders import Order
from .trucks import Truck
from .riders import Rider
from .deliveries import Delivery
from datetime import datetime

class DeliveryManagementSystem:
    
    def __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        Session =  sessionmaker(bind=self.engine)
        self.session=Session()
    
    def create_order(self, product, quantity, cost, customer_name, location ):

        order = Order(product=product, quantity=quantity, cost=cost, customer_name=customer_name, location=location)
        self.session.add(order)
        self.session.commit()
        print(f"\033[92m Success!! Entry saved at {datetime.now()} \033[0m")


if __name__ == '__main__':

    trial = DeliveryManagementSystem("dms_test.db")
    print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")
    trial.create_order("Laptop", 5, 2500, "Kimani", "Nairobi")
    print(f"\033[92m Success!! Entry Created at {datetime.now()} \033[0m")    