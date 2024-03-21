from db import delivery_management_system
from datetime import datetime

DMS = delivery_management_system.DeliveryManagementSystem
# Create DataBase
    
dms_db = DMS("dms.db")
print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")

def create_order(product, quantity, cost, customer_name, location):
    dms_db.create_order(product, quantity, cost, customer_name, location)
    print(f"\033[093m Success!! Order created.\033[0m")

def add_truck(reg_no, truck_capacity, model):
    dms_db.add_truck(reg_no, truck_capacity, model)
    print(f"\033[093m Success!! Truck {reg_no} Added.\033[0m")

def add_rider(name, location, truck_id):
    dms_db.add_rider(name, location, truck_id)
    print(f"\033[093m Success!! Rider {name} Added.\033[0m")





def exit_program():
    print("\033[093m Sad To See You Leave :-( See You Soon With More Orders!\033[0m")
    exit()