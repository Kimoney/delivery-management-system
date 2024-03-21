
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
        self.name = db_name
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        Session =  sessionmaker(bind=self.engine)
        self.session=Session()
        print("\033[32m =====Success!! Database Initialized!===== \033[0m")

    def __repr__(self):
        return (
            f"=====Success!! Database {self.name} Created Successfully"
        )
    
    def create_order(self, product, quantity, cost, customer_name, location ):

        order = Order(product=product, quantity=quantity, cost=cost, customer_name=customer_name, location=location)
        self.session.add(order)
        self.session.commit()
        print(f"\033[92m Success!! Order created at {datetime.now()} \033[0m")

    def add_truck(self, reg_no, truck_capacity, model):
        if not reg_no or not truck_capacity or not model:
            print("\033[31m Error: Reg. No, Truck Capacity and Model are required \033[0m")

        truck = Truck(reg_no=reg_no, truck_capacity=truck_capacity, model=model)

        try:
            self.session.add(truck)
            self.session.commit()
            print(f"\033[92m Success!! Truck saved at {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")
    

    def add_rider(self, name, location, truck_id):
        if not name or not location or not truck_id:
            print("\033[31m Error: Name, Location and Truck ID are required \033[0m")

        rider = Rider(name=name, location=location, truck_id=truck_id)

        try:
            self.session.add(rider)
            self.session.commit()
            print(f"\033[92m Success!! Rider added at {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

    def create_delivery(self, order_id, rider_id):
        delivery = Delivery(order_id=order_id, rider_id=rider_id)
        self.session.add(delivery)
        self.session.commit()
        print(f"\033[92m Success!! Delivery made at {datetime.now()} \033[0m")


if __name__ == '__main__':
    pass

    # trial = DeliveryManagementSystem("dms_test.db")
    # print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")
    # trial.create_order("Laptop", 5, 2500, "Kimani", "Nairobi")
    # print(f"\033[92m Success!! Order Created at {datetime.now()} \033[0m")
    # trial.add_truck("KDA 969K", 2500, "Mitsubishi FH")
    # print(f"\033[92m Success!! Truck Added at {datetime.now()} \033[0m")    