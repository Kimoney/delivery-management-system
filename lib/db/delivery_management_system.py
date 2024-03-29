
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
    
 #*****************************CREATE*****************************   
# CREATE ENTRIES
    # 1. Order
    
    def create_order(self, product, quantity, cost, customer_name, location ):

        order = Order(product=product.title(), quantity=quantity, cost=cost, customer_name=customer_name.title(), location=location.title())
        self.session.add(order)
        self.session.commit()
        print(f"\033[92m Success!! Order created at {datetime.now()} \033[0m")

    # 2. Truck

    def add_truck(self, reg_no, truck_capacity, model):
        if not reg_no or not truck_capacity or not model:
            print("\033[31m Error: Reg. No, Truck Capacity and Model are required \033[0m")

        truck = Truck(reg_no=reg_no.upper(), truck_capacity=truck_capacity, model=model.title())

        try:
            self.session.add(truck)
            self.session.commit()
            print(f"\033[92m Success!! Truck saved at {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: Reg No. Already Exists. Reg No. Has To Be Unique \033[0m")
            print(f"\033[31m Error: {e} \033[0m")

    # 3. Rider

    def add_rider(self, name, location, truck_id):
        if not name or not location or not truck_id:
            print("\033[31m Error: Name, Location and Truck ID are required \033[0m")

        rider = Rider(name=name.title(), location=location.title(), truck_id=truck_id)

        try:
            self.session.add(rider)
            self.session.commit()
            print(f"\033[92m Success!! Rider added at {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

    # 4. Delivery

    def create_delivery(self, order_id, rider_id):
        if not order_id or not rider_id:
            print("\033[31m Error: Order Id and Rider Id are required \033[0m")
            
        delivery = Delivery(order_id=order_id, rider_id=rider_id)

        try:
            self.session.add(delivery)
            self.session.commit()
            print(f"\033[92m Success!! Delivery made at {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

#*****************************READ*****************************
            
# GET ALL
    # 1.0 Orders(All)
        
    def get_all_orders(self):
        return self.session.query(Order).all()
    
    # 1.1 Order(Using ID)

    def get_order_by_id(self, id_):
        if not id_:
            print(f"\033[31m Error: Order Id is Required\033[0m")
        try:
            id_ = int(id_)
            if isinstance(id_, int):
                order = self.session.query(Order).filter_by(id=id_).one()
                return order
            else:
                raise Exception("\033[31m Error: Id Has To Be An Integer \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

    # 1.2 Order(Using Location)

    def get_order_by_location(self, location):
        if not location:
            print(f"\033[31m Error: Location is Required\033[0m")
        try:
            if isinstance(location, str):
                order = self.session.query(Order).filter_by(location=location.title()).all()
                return order
            else:
                raise Exception("\033[31m Error: Location Has To Be A String\033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")
    
    # 2. Truck
    # 2.0 Trucks(All)
        
    def get_all_trucks(self):
        return self.session.query(Truck).all()
    
    # 2.1 Truck(Using ID)

    def get_truck_by_id(self, id_):
        if not id_:
            print(f"\033[31m Error: Truck Id is Required\033[0m")
        try:
            id_ = int(id_)
            if isinstance(id_, int):
                truck = self.session.query(Truck).filter_by(id=id_).one()
                return truck
            else:
                raise Exception("\033[31m Error: Id Has To Be An Integer \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

    
    # 2.2 Truck(Using Reg. No.)

    def get_truck_by_reg_no(self, reg_no):
        if not reg_no:
            print(f"\033[31m Error: Truck Reg No. is Required\033[0m")
        try:
            if isinstance(reg_no, str):
                truck = self.session.query(Truck).filter_by(reg_no=reg_no.upper()).one()
                return truck
            else:
                raise Exception("\033[31m Error: Reg. No. Has To Be A String\033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")
    
    # 2.2 Truck(Using Model)

    def get_truck_by_model(self, model):
        if not model:
            print(f"\033[31m Error: Truck Model is Required\033[0m")
        try:
            if isinstance(model, str):
                truck = self.session.query(Truck).filter_by(model=model.title()).all()
                return truck
            else:
                raise Exception("\033[31m Error: Model Has To Be A String\033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")
    
    # 2.3 All Trucks Assigned To Riders
            
    def get_assigned_trucks(self):
        # Subquery to get IDs of trucks that have corresponding records in riders table
        subquery = self.session.query(Rider.truck_id).distinct()
        print(subquery)
        # Retrieve trucks whose IDs are in the subquery
        return self.session.query(Truck).filter(Truck.id.in_(subquery)).all()
            
    # 2.5 All Unassigned Trucks
       
    def get_all_unassigned_trucks(self):
        # Subquery to get IDs of trucks that have corresponding records in riders table
        subquery = self.session.query(Rider.truck_id).distinct()
        # Retrieve trucks whose IDs are not in the subquery
        return self.session.query(Truck).filter(not_(Truck.id.in_(subquery))).all()
    
    # 3.0 Rider
        
    def get_all_riders(self):
        return self.session.query(Rider).all()
    
    # 3.1 Rider(Using ID)

    def get_rider_by_id(self, id_):
        if not id_:
            print(f"\033[31m Error: Rider Id is Required\033[0m")
        try:
            id_ = int(id_)
            if isinstance(id_, int):
                rider = self.session.query(Rider).filter_by(id=id_).one()
                return rider
            else:
                raise Exception("\033[31m Error: Id Has To Be An Integer \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

    # 3.1 Rider(Using Location)
            
    def get_rider_by_location(self, location):
        if not location:
            print(f"\033[31m Error: Rider Id is Required\033[0m")
        try:
            if isinstance(location, str):
                rider = self.session.query(Rider).filter_by(location=location.title()).one()
                return rider
            else:
                raise Exception("\033[31m Error: Id Has To Be An Integer \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")
    
    # 4. Delivery (Completed)
        
    def get_all_completed_deliveries(self):
        return self.session.query(Delivery).all()
    
    # 4.1. Delivery(Pending)
        
    def get_all_pending_deliveries(self):
        # Subquery to get IDs of orders that have corresponding records in Delivery table
        subquery = self.session.query(Delivery.order_id).distinct()
        # Retrieve orders whose IDs are not in the subquery
        return self.session.query(Order).filter(not_(Order.id.in_(subquery))).all()
    
    # 4.2 Delivery(Using ID)

    def get_delivery_by_id(self, id_):
        if not id_:
            print(f"\033[31m Error: Delivery Id is Required\033[0m")
        try:
            id_ = int(id_)
            if isinstance(id_, int):
                delivery = self.session.query(Delivery).filter_by(id=id_).one()
                return delivery
            else:
                raise Exception("\033[31m Error: Id Has To Be An Integer \033[0m")
        except Exception as e:
            self.session.rollback()
            print(f"\033[31m Error: {e} \033[0m")

#*****************************UPDATE*****************************
    # 1. Orders

    def update_order(self, id_, product, quantity, cost, customer_name, location):
        if not id_ or not product or not quantity or not cost or not customer_name or not location:
            print("\033[31m Error: ORDER ID, PRODUCT, QUANTITY, COST, CUSTOMER NAME, LOCATION are all required.\033[0m")

# Step 1: Query the Order to update using its primary key
        order = self.session.query(Order).get(id_)

# Step 2: Modify the attributes of the queried Order
        try:
            order.product = product.title()
            order.quantity = quantity
            order.cost = cost
            order.customer_name = customer_name.title()
            order.location = location.title()
            self.session.commit()
            print(f"\033[92m Success!! Order Updated{datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: ORDER ID, PRODUCT, QUANTITY, COST, CUSTOMER NAME, LOCATION are all required.\033[0m")
            print(f"\033[31m Error: {e} \033[0m")



    # 2. Trucks

    def update_truck(self, id_, reg_no, truck_capacity, model):
        if not id_ or not reg_no or not truck_capacity or not model:
            print("\033[31m Error: TRUCK ID, REG No.(Has To Be Unique), TRUCK CAPACITY are all required. \033[0m")

# Step 1: Query the Truck to update using its primary key
        truck = self.session.query(Truck).get(id_)

# Step 2: Modify the attributes of the queried Truck
        try:
            truck.reg_no = reg_no.upper()
            truck.truck_capacity = truck_capacity
            truck.model = model.title()
            self.session.commit()
            print(f"\033[92m Success!! Truck Updated{datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: TRUCK ID, REG No.(Has To Be Unique), TRUCK CAPACITY are all required. \033[0m")
            print(f"\033[31m Error: {e} \033[0m")


    # 3. Riders

    def update_rider(self, id_, location, truck_id):
        if not id_ or not location or not truck_id:
            print("\033[31m Error: Rider id and an unassigned location & Truck are required \033[0m")

# Step 1: Query the Rider to update using its primary key
        rider = self.session.query(Rider).get(id_)

# Step 2: Modify the attributes of the queried Rider
        try:
            rider.location = location.title()
            rider.truck_id = truck_id
            self.session.commit()
            print(f"\033[92m Success!! Rider Re-Assigned{datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: RIDER ID, an UNASSIGNED LOCATION, and an UNASSIGNED TRUCK are required \033[0m")
            print(f"\033[31m Error: {e} \033[0m")

    # 4. Deliveries
            
    def update_delivery(self, id_, order_id, rider_id):
        if not id_ or not order_id or not rider_id:
            print("\033[31m Error: DELIVERY ID, ORDER ID and RIDER ID ARE REQUIRED \033[0m")

# Step 1: Query the Delivery to update using its primary key
        delivery = self.session.query(Delivery).get(id_)

# Step 2: Modify the attributes of the queried Delivery
        try:
            delivery.order_id = order_id
            delivery.rider_id = rider_id
            self.session.commit()
            print(f"\033[92m Success!! Delivery Updated!! {datetime.now()} \033[0m")
        except Exception as e:
            self.session.rollback()
            print("\033[31m Error: DELIVERY ID, ORDER ID and RIDER ID ARE REQUIRED \033[0m")
            print(f"\033[31m Error: {e} \033[0m")

#*****************************DELETE*****************************
    # 1. Orders
        
    def delete_order(self, id_):
        if not id_:
            print("\033[31m Error: ORDER ID is required. \033[0m")
    # Step 1: Query the Order to update using its primary key
        order = self.session.query(Order).get(id_)
    # Step 2: If the row exists, delete it
        if order:
            self.session.delete(order)
    # Step 3: Commit the transaction
            self.session.commit()
            print(f"\033[31m ORDER ID {id_} DELETED SUCCESSFULLY!! \033[0m")
            
    # 2. Trucks

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

    # 3. Riders
            
    def delete_rider(self, id_):
        if not id_:
            print("\033[31m Error: Rider ID is required. \033[0m")
    # Step 1: Query the Rider to update using its primary key
        rider = self.session.query(Rider).get(id_)
    # Step 2: If the row exists, delete it
        if rider:
            self.session.delete(rider)
    # Step 3: Commit the transaction
            self.session.commit()
            print(f"\033[31m RIDER ID {id_} DELETED SUCCESSFULLY!! \033[0m")
            
    # 4. Deliveries
            
    def delete_delivery(self, id_):
        if not id_:
            print("\033[31m Error: Delivery ID is required. \033[0m")
    # Step 1: Query the Delivery to update using its primary key
        delivery = self.session.query(Delivery).get(id_)
    # Step 2: If the row exists, delete it
        if delivery:
            self.session.delete(delivery)
    # Step 3: Commit the transaction
            self.session.commit()
            print(f"\033[31m DELIVERY ID {id_} DELETED SUCCESSFULLY!! \033[0m")