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
    dms_db.create_delivery(order_id, rider_id)
    print(f"\033[093m Success!! Delivery made at {datetime.now()}.\033[0m")

# GET ALL FUNCTIONS

def get_all_orders():
    orders = dms_db.get_all_orders()
    print(f"\033[032m\033[1m *********Orders As {datetime.now()} ********* \033[0m")

    for order in orders:
        print(f"\033[036m<Order No.: {order.id} | Customer: {order.customer_name} | Product :{order.product} | Quantity: {order.quantity} | Amount: {order.cost} | Location: {order.location}> \033[0m")

def get_all_trucks():
    trucks = dms_db.get_all_trucks()
    print(f"\033[032m\033[1m *********Your Fleet At {datetime.now()} ********* \033[0m")

    for truck in trucks:
        print(f"\033[036m<Truck ID.: {truck.id} | Registration No.: {truck.reg_no} | Capacity: {truck.truck_capacity}cc | Model: {truck.model}> \033[0m")

def get_all_riders():
    riders = dms_db.get_all_riders()
    print(f"\033[032m\033[1m *********Your Riders As At {datetime.now()} ********* \033[0m")

    for rider in riders:
        print(f"\033[036m<Rider Id: {rider.id} | Assigned Truck: {rider.truck_id} | Location: {rider.location} | Name: {rider.name}> \033[0m")

def exit_program():
    print("\033[093m Sad To See You Leave :-( See You Soon With More Orders!\033[0m")
    exit()