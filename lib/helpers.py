from db import delivery_management_system

DMS = delivery_management_system.DeliveryManagementSystem

def helper_1():
    print("Performing useful function#1.")

def create_database(db_name):
    db_name = db_name.lower()
    DMS(f"{db_name}.db")
    print(f"\033[093m Success!! Database {db_name}.db created.\033[0m")

def create_order(product, quantity, cost, customer_name, location):
    DMS.create_order(product, quantity, cost, customer_name, location)
    print(f"\033[093m Success!! Order created.\033[0m")




def exit_program():
    print("\033[093m Sad To See You Leave :-( See You Soon With More Orders!\033[0m")
    exit()