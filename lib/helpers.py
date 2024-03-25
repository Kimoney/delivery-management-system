from db import delivery_management_system
from datetime import datetime
from tabulate import tabulate

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
# ================================ORDERS================================

def get_all_orders():
    orders = dms_db.get_all_orders()
    print(f"\033[032m\033[1m *********Orders As {datetime.now()} ********* \033[0m")

    order_details = [
        ["\033[036m\033[1mOrder No.", "Customer Name", "Product","Quantity","Amount","Location\033[0m"]
    ]
    for order in orders:
        order_details.append([
            f"\033[036m{order.id}",
            order.customer_name,
            order.product,
            order.quantity,
            order.cost,
            f"{order.location}\033[0m"
        ])
    # Print Table
    print(tabulate(order_details, headers="firstrow", tablefmt="fancy_outline"))

def get_order_by_id(id_):
    order = dms_db.get_order_by_id(id_)
    order_details = [
        ["\033[036m\033[1mOrder No.", "Customer Name", "Product","Quantity","Amount","Location\033[0m"]
    ]
    if order:
        order_details.append([
            f"\033[036m{order.id}",
            order.customer_name,
            order.product,
            order.quantity,
            order.cost,
            f"{order.location}\033[0m"
        ])
    # Print Table
        print(tabulate(order_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Order With Id {id_} Doesn't Exist!!!\033[0m")

def get_order_by_location(location):
    orders = dms_db.get_order_by_location(location)
    order_details = [
        ["\033[036m\033[1mOrder No.", "Customer Name", "Product","Quantity","Amount","Location\033[0m"]
    ]
    if orders:
        for order in orders:
            order_details.append([
            f"\033[036m{order.id}",
            order.customer_name,
            order.product,
            order.quantity,
            order.cost,
            f"{order.location}\033[0m"
        ])
    # Print Table
        print(tabulate(order_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m No Orders Destined For {location} Found!!!\033[0m")

# ================================TRUCKS================================

def get_all_trucks():
    trucks = dms_db.get_all_trucks()
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    print(f"\033[032m\033[1m *********Your Fleet At {datetime.now()} ********* \033[0m")
    for truck in trucks:
        truck_details.append([
            f"\033[036m{truck.id}",
            truck.reg_no,
            truck.truck_capacity,
            f"{truck.model}\033[0m"
        ])
    # Print Table
    print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))

def get_truck_by_id(id_):
    truck = dms_db.get_truck_by_id(id_)
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    if truck:
        print(f"\033[032m\033[1m ********* Truck {id_} Details on {datetime.now()} ********* \033[0m")
        truck_details.append([
            f"\033[036m{truck.id}",
            truck.reg_no,
            truck.truck_capacity,
            f"{truck.model}\033[0m"
        ])
    # Print Table
        print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Truck With Id {id_} Doesn't Exist!!!\033[0m")

def get_truck_by_reg_no(reg_no):
    truck = dms_db.get_truck_by_reg_no(reg_no)
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    if truck:
        print(f"\033[032m\033[1m ********* Truck {reg_no.upper()} Details on {datetime.now()} ********* \033[0m")
        truck_details.append([
            f"\033[036m{truck.id}",
            truck.reg_no,
            truck.truck_capacity,
            f"{truck.model}\033[0m"
        ])
    # Print Table
        print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Truck {reg_no} Doesn't Exist!!!\033[0m")
    
def get_truck_by_model(model):
    trucks = dms_db.get_truck_by_model(model)
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    if trucks:
        print(f"\033[032m\033[1m *********{model.title()} Trucks In Your Fleet As At {datetime.now()} ********* \033[0m")
        for truck in trucks:
            truck_details.append([
            f"\033[036m{truck.id}",
            truck.reg_no,
            truck.truck_capacity,
            f"{truck.model}\033[0m"
        ])
    # Print Table
        print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Truck {model} Doesn't Exist!!!\033[0m")
    
def get_assigned_trucks():
    trucks = dms_db.get_assigned_trucks()
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    print(f"\033[032m\033[1m *********Assigned Trucks As At {datetime.now()} ********* \033[0m")
    for truck in trucks:
        truck_details.append([
        f"\033[036m{truck.id}",
        truck.reg_no,
        truck.truck_capacity,
        f"{truck.model}\033[0m"
        ])
    # Print Table
    print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))

def get_all_unassigned_trucks():
    trucks = dms_db.get_all_unassigned_trucks()
    truck_details = [
        ["\033[036m\033[1mTruck ID", "Registration No", "Truck Capacity","Model\033[0m"]
    ]
    print(f"\033[032m\033[1m *********Unassigned Trucks As At {datetime.now()} ********* \033[0m")
    for truck in trucks:
        truck_details.append([
        f"\033[036m{truck.id}",
        truck.reg_no,
        truck.truck_capacity,
        f"{truck.model}\033[0m"
        ])
    # Print Table
    print(tabulate(truck_details, headers="firstrow", tablefmt="fancy_outline"))

# ================================RIDERS================================
        
def get_all_riders():
    riders = dms_db.get_all_riders()
    rider_details = [
        ["\033[036m\033[1mRider ID", "Truck ID", "Location","Name\033[0m"]
    ]
    print(f"\033[032m\033[1m *********Your Riders As At {datetime.now()} ********* \033[0m")
    for rider in riders:
        rider_details.append([
        f"\033[036m{rider.id}",
        rider.truck_id,
        rider.location,
        f"{rider.name}\033[0m"
        ])
    # Print Table
    print(tabulate(rider_details, headers="firstrow", tablefmt="fancy_outline"))


def get_rider_by_id(id_):
    rider = dms_db.get_rider_by_id(id_)
    rider_details = [
        ["\033[036m\033[1mRider ID", "Truck ID", "Location","Name\033[0m"]
    ]
    if rider:
        print(f"\033[032m\033[1m ********* Rider {id_} Details as at {datetime.now()} ********* \033[0m")
        rider_details.append([
        f"\033[036m{rider.id}",
        rider.truck_id,
        rider.location,
        f"{rider.name}\033[0m"
        ])
    # Print Table
        print(tabulate(rider_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Rider With Id {id_} Doesn't Exist!!!\033[0m")

def get_rider_by_location(location):
    rider = dms_db.get_rider_by_location(location)
    rider_details = [
        ["\033[036m\033[1mRider ID", "Truck ID", "Location","Name\033[0m"]
    ]
    if rider:
        print(f"\033[032m\033[1m ********* Rider {location.title()} Details as at {datetime.now()} ********* \033[0m")
        rider_details.append([
        f"\033[036m{rider.id}",
        rider.truck_id,
        rider.location,
        f"{rider.name}\033[0m"
        ])
    # Print Table
        print(tabulate(rider_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m No Riders In {location}.\nYou, Can Assign One Using the `Manage Supply Chain` option!!\033[0m")

# View Rider's Completed Deliveries
    
def a_riders_completed_deliveries(id_):
    deliveries = dms_db.get_all_completed_deliveries()
    delivery_details = [
        ["\033[036m\033[1mDelivery ID", "Order ID", "Time","Rider ID\033[0m"]
    ]
    id_ = int(id_)
    rider = dms_db.get_rider_by_id(id_)
    if rider:
        print(f"\033[032m\033[1m *********{dms_db.get_rider_by_id(id_).name}'s Completed Deliveries As At {datetime.now()}********* \033[0m")
        for delivery in deliveries:
            if delivery.rider_id == id_:
                delivery_details.append([
                f"\033[036m{delivery.id}",
                delivery.order_id,
                delivery.time,
                f"{delivery.rider_id}\033[0m"
                ])
    # Print Table
        print(tabulate(delivery_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        print("\033[31mEnter A Valid Rider ID\033[0m")

# View Rider's Pending Deliveries
    
def a_riders_pending_deliveries(id_):
    id_ = int(id_)
    rider = dms_db.get_rider_by_id(id_)
    deliveries = dms_db.get_all_completed_deliveries()
    delivery_details = [
        ["\033[036m\033[1mOrder ID", "Customer", "Product", "Quantity", "Amount", "Location\033[0m"]
    ]
    if rider:
        riders_orders = dms_db.get_order_by_location(rider.location)
        pending_deliveries = [order for order in riders_orders if order.id not in {delivery.order_id for delivery in deliveries}]

        if pending_deliveries:
            for pending in pending_deliveries:
                delivery_details.append([
                f"\033[036m{pending.id}",
                pending.customer_name,
                pending.product,
                pending.quantity,
                pending.cost,
                f"{pending.location}\033[0m"
                ])
    # Print Table
            print(tabulate(delivery_details, headers="firstrow", tablefmt="fancy_outline"))
        else:
            print("\033[031m<No Pending Deliveries Found!>\033[0m")
    else:
        print("\033[31mEnter A Valid Rider ID\033[0m")

# ================================DELIVERIES================================

def get_all_completed_deliveries():
    deliveries = dms_db.get_all_completed_deliveries()
    delivery_details = [
        ["\033[036m\033[1mDelivery ID", "Order ID", "Time","Rider ID\033[0m"]
    ]
    print(f"\033[032m\033[1m *********All Completed Deliveries As At {datetime.now()} ********* \033[0m")
    for delivery in deliveries:
        delivery_details.append([
                f"\033[036m{delivery.id}",
                delivery.order_id,
                delivery.time,
                f"{delivery.rider_id}\033[0m"
                ])
    # Print Table
    print(tabulate(delivery_details, headers="firstrow", tablefmt="fancy_outline"))

def get_all_pending_deliveries():
    pending_deliveries = dms_db.get_all_pending_deliveries()
    delivery_details = [
        ["\033[036m\033[1mOrder ID", "Customer", "Product", "Quantity", "Amount", "Location\033[0m"]
    ]
    print(f"\033[032m\033[1m *********All Pending Deliveries As At {datetime.now()} ********* \033[0m")
    for pending in pending_deliveries:
        delivery_details.append([
                f"\033[036m{pending.id}",
                pending.customer_name,
                pending.product,
                pending.quantity,
                pending.cost,
                f"{pending.location}\033[0m"
                ])
    # Print Table
    print(tabulate(delivery_details, headers="firstrow", tablefmt="fancy_outline"))

def get_delivery_by_id(id_):
    delivery = dms_db.get_delivery_by_id(id_)
    delivery_details = [
        ["\033[036m\033[1mDelivery ID", "Order ID", "Time","Rider ID\033[0m"]
    ]
    if delivery:
        print(f"\033[032m\033[1m ********* Delivery {id_} Details as at {datetime.now()} ********* \033[0m")
        delivery_details.append([
                f"\033[036m{delivery.id}",
                delivery.order_id,
                delivery.time,
                f"{delivery.rider_id}\033[0m"
                ])
    # Print Table
        print(tabulate(delivery_details, headers="firstrow", tablefmt="fancy_outline"))
    else:
        return print(f"\033[31m Delivery With Id {id_} Doesn't Exist!!!\033[0m")

# Delivery Status

def delivery_status(id_):
    id_ = int(id_)
    order = dms_db.get_order_by_id(id_)
    completed_deliveries = dms_db.get_all_completed_deliveries()
    pending_deliveries = dms_db.get_all_pending_deliveries()
    if order:
        # Code here
        if order.id in [delivery.order_id for delivery in completed_deliveries]:
            print(f"\033[032m\033[1m ********* Order {id_} Has Already Been Delivered ********* \033[0m")
        elif order.id in [pending_order.id for pending_order in pending_deliveries]:
            print(f"\033[032m\033[1m ********* Order {id_} Has Not Been Delivered ********* \033[0m")
        else:
            print(f"\033[032m\033[1m ********* Order {id_} Status Unknown********* \033[0m")
    else:
        print("\033[31mEnter A Valid Order ID\033[0m")

# UPDATE METHODS

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
    order = dms_db.get_order_by_id(id_)
    if order:
        dms_db.delete_order(id_)
        print(f"\033[31mOrder Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mOrder Id: {id_} Doesn't Exist!!!\033[0m")
    
def delete_truck(id_):
    truck = dms_db.get_truck_by_id(id_)
    if truck:
        dms_db.delete_truck(id_)
        print(f"\033[31mTruck Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mTruck Id: {id_} Doesn't Exist!!!\033[0m")

def delete_rider(id_):
    rider = dms_db.get_rider_by_id(id_)
    if rider:
        dms_db.delete_rider(id_)
        print(f"\033[31mRider Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mRider Id: {id_} Doesn't Exist!!!\033[0m")

def delete_delivery(id_):
    delivery = dms_db.get_delivery_by_id(id_)
    if delivery:
        dms_db.delete_delivery(id_)
        print(f"\033[31mDelivery Id: {id_} Successfully Deleted!!\033[0m")
    else:
        print(f"\033[31mDelivery Id: {id_} Doesn't Exist!!!\033[0m")

def exit_program():
    print("\033[92mTime To Say Goodbye! 👋🚚 \nDon't Worry, Your Deliveries Are In Safe Hands! 📦😄\nCatch You Later, With More Orders! 📦🚀\033[0m")
    exit()