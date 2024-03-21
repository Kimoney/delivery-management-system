
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
        print(f"\033[92m Success!! Order created at {datetime.now()} \033[0m")

    def add_truck(self, reg_no, truck_capacity, model):

        truck = Truck(reg_no=reg_no, truck_capacity=truck_capacity, model=model)
        self.session.add(truck)
        self.session.commit()
        print(f"\033[92m Success!! Truck saved at {datetime.now()} \033[0m")


if __name__ == '__main__':

    trial = DeliveryManagementSystem("dms_test.db")
    print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")
    trial.create_order("Laptop", 5, 2500, "Kimani", "Nairobi")
    print(f"\033[92m Success!! Order Created at {datetime.now()} \033[0m")
    trial.add_truck("KDA 567K", 2500, "Mitsubishi FH")
    print(f"\033[92m Success!! Truck Added at {datetime.now()} \033[0m")    