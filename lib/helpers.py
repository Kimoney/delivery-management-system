from db import delivery_management_system
from datetime import datetime

DMS = delivery_management_system.DeliveryManagementSystem
# Create DataBase
    
dms_db = DMS("dms.db")
print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")

# CREATE RECORDS ON TABLES

def create_order(product, quantity, cost, customer_name, location):
    dms_db.create_order(product, quantity, cost, customer_name, location)
    print(f"\033[093m Success!! Order created.\033[0m")

def add_truck(reg_no, truck_capacity, model):
    dms_db.add_truck(reg_no, truck_capacity, model)
    print(f"\033[093m Success!! Truck {reg_no} Added.\033[0m")

def add_rider(name, location, truck_id):
    dms_db.add_rider(name, location, truck_id)
    print(f"\033[093m Success!! Rider {name} Added.\033[0m")

def create_delivery(order_id, rider_id):
    order = dms_db.get_order_by_id(order_id)
    rider = dms_db.get_rider_by_id(rider_id)
    if order.location.title() == rider.location.title():
        dms_db.create_delivery(order_id, rider_id)
        order = dms_db.get_order_by_id(order_id)
        print(f"\033[093m Delivery Confirmed! {order.customer_name} has recieved {order.quantity} {order.product} at {datetime.now()}. Amount: {order.cost} \033[0m")
    else:
        print("\033[31m Error: You Can't Deliver Orders Not Designated For Your Assigned Location.\nContact Admin If You Have To Deliver The Order! \033[0m")

# GET ALL FUNCTIONS

def get_all_orders():
    orders = dms_db.get_all_orders()
    print(f"\033[032m\033[1m *********Orders As {datetime.now()} ********* \033[0m")

    for order in orders:
        print(f"\033[036m<Order No.: {order.id} | Customer: {order.customer_name} | Product :{order.product} | Quantity: {order.quantity} | Amount: KES {order.cost} | Location: {order.location}> \033[0m")

def get_order_by_id(id_):
    order = dms_db.get_order_by_id(id_)
    if order:
        print(f"\033[036m<Order No.: {order.id} | Customer: {order.customer_name} | Product :{order.product} | Quantity: {order.quantity} | Amount: {order.cost} | Location: {order.location}> \033[0m")
    else:
        return print(f"\033[31m Order With Id {id_} Doesn't Exist!!!\033[0m")

def get_order_by_location(location):
    orders = dms_db.get_order_by_location(location)

    if orders:

        for order in orders:
            print(f"\033[036m<Order No.: {order.id} | Customer: {order.customer_name} | Product :{order.product} | Quantity: {order.quantity} | Amount: {order.cost} | Location: {order.location}> \033[0m")
    else:
        return print(f"\033[31m No Orders Destined For {location} Found!!!\033[0m")

def get_all_trucks():
    trucks = dms_db.get_all_trucks()
    print(f"\033[032m\033[1m *********Your Fleet At {datetime.now()} ********* \033[0m")

    for truck in trucks:
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")

def get_truck_by_id(id_):
    truck = dms_db.get_truck_by_id(id_)
    if truck:
        print(f"\033[032m\033[1m ********* Truck {id_} Details on {datetime.now()} ********* \033[0m")
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")
    else:
        return print(f"\033[31m Truck With Id {id_} Doesn't Exist!!!\033[0m")

def get_truck_by_reg_no(reg_no):
    truck = dms_db.get_truck_by_reg_no(reg_no)
    if truck:
        print(f"\033[032m\033[1m ********* Truck {reg_no}'s Details on {datetime.now()} ********* \033[0m")
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")
    else:
        return print(f"\033[31m Truck {reg_no} Doesn't Exist!!!\033[0m")
    
def get_truck_by_model(model):
    trucks = dms_db.get_truck_by_model(model)
    if trucks:
        print(f"\033[032m\033[1m *********{model} Trucks In Your Fleet As At {datetime.now()} ********* \033[0m")
        for truck in trucks:
            print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")
    else:
        return print(f"\033[31m Truck {model} Doesn't Exist!!!\033[0m")
    
def get_assigned_trucks():
    trucks = dms_db.get_assigned_trucks()
    print(f"\033[032m\033[1m *********Assigned Trucks As At {datetime.now()} ********* \033[0m")
    for truck in trucks:
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")

def get_all_unassigned_trucks():
    trucks = dms_db.get_all_unassigned_trucks()
    print(f"\033[032m\033[1m *********Unassigned Trucks As At {datetime.now()} ********* \033[0m")
    for truck in trucks:
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")

# ================================RIDERS================================
        
def get_all_riders():
    riders = dms_db.get_all_riders()
    print(f"\033[032m\033[1m *********Your Riders As At {datetime.now()} ********* \033[0m")

    for rider in riders:
        print(f"\033[036m<Rider Id: {rider.id} | Assigned Truck: {rider.truck_id} | Location: {rider.location} | Name: {rider.name}> \033[0m")

def get_rider_by_id(id_):
    rider = dms_db.get_rider_by_id(id_)
    if rider:
        print(f"\033[032m\033[1m ********* Rider {id_} Details as at {datetime.now()} ********* \033[0m")
        print(f"\033[036m<Rider Id: {rider.id} | Assigned Truck: {rider.truck_id} | Location: {rider.location} | Name: {rider.name}> \033[0m")
    else:
        return print(f"\033[31m Rider With Id {id_} Doesn't Exist!!!\033[0m")

def get_rider_by_location(location):
    rider = dms_db.get_rider_by_location(location)
    if rider:
        print(f"\033[032m\033[1m *********{location} Rider's Details as at {datetime.now()} ********* \033[0m")
        print(f"\033[036m<Rider Id: {rider.id} | Assigned Truck: {rider.truck_id} | Location: {rider.location} | Name: {rider.name}> \033[0m")
    else:
        return print(f"\033[31m No Riders In {location}.\nYou, Can Assign One Using the `Manage Supply Chain` option!!\033[0m")

def get_all_completed_deliveries():
    deliveries = dms_db.get_all_completed_deliveries()
    print(f"\033[032m\033[1m *********All Completed Deliveries As At {datetime.now()} ********* \033[0m")

    for delivery in deliveries:
        print(f"\033[036m<Delivery Id: {delivery.id} | Order: {delivery.order_id} | Completed At: {delivery.time} | By Rider {delivery.rider_id} > \033[0m")

def get_all_pending_deliveries():
    pending_deliveries = dms_db.get_all_pending_deliveries()
    print(f"\033[032m\033[1m *********All Pending Deliveries As At {datetime.now()} ********* \033[0m")

    for pending in pending_deliveries:
        print(f"\033[036m<Delivery Id: {None} | Order: {pending.id} | Customer: {pending.customer_name} | Product :{pending.product} | Quantity: {pending.quantity} | Amount: {pending.cost} | Location: {pending.location}> \033[0m")

def update_order(id_, product, quantity, cost, customer_name, location):
    dms_db.update_order(id_, product, quantity, cost, customer_name, location)
    print(f"\033[093m Success!! Changes Implemented on Order {id_} {datetime.now()}.\033[0m")

def update_truck(id_, reg_no, truck_capacity, model):
    dms_db.update_truck(id_, reg_no, truck_capacity, model)
    print(f"\033[093m Success!! Rider Assignment Completed at {datetime.now()}.\033[0m")

def update_rider(id_, location, truck_id):
    dms_db.update_rider(id_, location, truck_id)
    print(f"\033[093m Success!! Rider Assignment Completed at {datetime.now()}.\033[0m")

#*************************DELETE*************************


def delete_order(id_):
    if dms_db.delete_order(id_):
        print(f"\033[31mOrder Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mOrder Id: {id_} Doesn't Exist!!!\033[0m")
    
def delete_truck(id_):
    if dms_db.delete_truck(id_):
        print(f"\033[31mTruck Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mTruck Id: {id_} Doesn't Exist!!!\033[0m")

def delete_rider(id_):
    if dms_db.delete_rider(id_):
        print(f"\033[31mRider Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mRider Id: {id_} Doesn't Exist!!!\033[0m")

def delete_delivery(id_):
    if dms_db.delete_delivery(id_):
        print(f"\033[31mDelivery Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mDelivery Id: {id_} Doesn't Exist!!!\033[0m")

def exit_program():
    print("\033[92mTime To Say Goodbye! 👋🚚 \nDon't Worry, Your Deliveries Are In Safe Hands! 📦😄\nCatch You Later, With More Orders! 📦🚀\033[0m")
    exit()