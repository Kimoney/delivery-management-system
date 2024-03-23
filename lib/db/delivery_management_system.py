
from sqlalchemy import create_engine, not_
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
    
# CREATE ENTRIES
    # 1. Order
    
    def create_order(self, product, quantity, cost, customer_name, location ):

        order = Order(product=product, quantity=quantity, cost=cost, customer_name=customer_name, location=location)
        self.session.add(order)
        self.session.commit()
        print(f"\033[92m Success!! Order created at {datetime.now()} \033[0m")

    # 1. Truck

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
            print("\033[31m Error: Reg No. Already Exists. Reg No. Has To Be Unique \033[0m")
            print(f"\033[31m Error: {e} \033[0m")

    # 1. Rider

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

    # 1. Delivery

    def create_delivery(self, order_id, rider_id):
        delivery = Delivery(order_id=order_id, rider_id=rider_id)
        self.session.add(delivery)
        self.session.commit()
        print(f"\033[92m Success!! Delivery made at {datetime.now()} \033[0m")

# GET ALL
    # 1. Orders
        
    def get_all_orders(self):
        return self.session.query(Order).all()
    
    # 1. Truck
        
    def get_all_trucks(self):
        return self.session.query(Truck).all()
    
    # 1. Rider
        
    def get_all_riders(self):
        return self.session.query(Rider).all()
    
    # 1. Delivery (Completed)
        
    def get_all_completed_deliveries(self):
        return self.session.query(Delivery).all()
    
    # 1. Delivery (Pending)
        
    def get_all_pending_deliveries(self):
        # Subquery to get IDs of orders that have corresponding records in Delivery table
        subquery = self.session.query(Delivery.order_id).distinct()
        # Retrieve orders whose IDs are not in the subquery
        return self.session.query(Order).filter(not_(Order.id.in_(subquery))).all()

# Update
    # 1. Orders

    # 2. Trucks

    def update_truck(self, id_, reg_no, truck_capacity, model):
        if not id_:
            print("\033[31m Error: TRUCK ID, REG No.(Has To Be Unique), TRUCK CAPACITY are all required. \033[0m")

# Step 1: Query the Truck to update using its primary key
        truck = self.session.query(Truck).get(id_)

# Step 2: Modify the attributes of the queried rider
        try:
            truck.reg_no = reg_no
            truck.truck_capacity = truck_capacity
            truck.model = model
            self.session.commit()
            print(f"\033[92m Success!! Truck Updated{datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: TRUCK ID, REG No.(Has To Be Unique), TRUCK CAPACITY are all required. \033[0m")
            print(f"\033[31m Error: {e} \033[0m")


    # 3. Riders

    def update_rider(self, id_, location, truck_id):
        if not id_:
            print("\033[31m Error: Rider id is required and an unassigned location & Truck \033[0m")

# Step 1: Query the rider to update using its primary key
        rider = self.session.query(Rider).get(id_)

# Step 2: Modify the attributes of the queried rider
        try:
            rider.location = location
            rider.truck_id = truck_id
            self.session.commit()
            print(f"\033[92m Success!! Rider Re-Assigned{datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: RIDER ID, an UNASSIGNED LOCATION, and an UNASSIGNED TRUCK are required \033[0m")
            print(f"\033[31m Error: {e} \033[0m")

    # 4. Deliveries
            
# DELETE
    # 1. Orders
            
    # 1. Trucks
    def delete_truck(self, id_):
        if not id_:
            print("\033[31m Error: TRUCK ID is required. \033[0m")
    # Step 1: Query the Truck to update using its primary key
        truck = self.session.query(Truck).get(id_)
    # Step 2: If the row exists, delete it
        if truck:
            self.session.delete(truck)
    # Step 3: Commit the transaction
            self.session.commit()
            print(f"\033[31m TRUCK ID {id_} DELETED SUCCESSFULLY!! \033[0m")

    # 1. Riders
    def delete_rider(self, id_):
        if not id_:
            print("\033[31m Error: Rider ID is required. \033[0m")
    # Step 1: Query the Truck to update using its primary key
        rider = self.session.query(Rider).get(id_)
    # Step 2: If the row exists, delete it
        if rider:
            self.session.delete(rider)
    # Step 3: Commit the transaction
            self.session.commit()
            print(f"\033[31m RIDER ID {id_} DELETED SUCCESSFULLY!! \033[0m")
            
    # 1. Deliveries


if __name__ == '__main__':
    pass

    # trial = DeliveryManagementSystem("dms_test.db")
    # print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")
    # trial.create_order("Laptop", 5, 2500, "Kimani", "Nairobi")
    # print(f"\033[92m Success!! Order Created at {datetime.now()} \033[0m")
    # trial.add_truck("KDA 969K", 2500, "Mitsubishi FH")
    # print(f"\033[92m Success!! Truck Added at {datetime.now()} \033[0m")    