from helpers import (
    exit_program,
    create_order,
    add_truck,
    add_rider,
    create_delivery,
    get_all_orders,
    get_all_trucks,
    get_all_riders,
    get_all_completed_deliveries,
    get_all_pending_deliveries,
    update_rider
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            while True:
                manage_supply_chain()
                choice = input("> ")
                if choice == "0":
                    main()
                elif choice == "1":
                    reg_no = input("Enter Truck's Registration Number: >")
                    truck_capacity = input("Enter Truck's Load Capacity: >")
                    model = input("Enter Truck's model: >")
                    add_truck(reg_no, truck_capacity, model)
                elif choice == "2":
                    name = input("Enter rider's name: ")
                    location = input("Enter rider's route location: ")
                    truck_id = input("Enter rider's truck id: ")
                    add_rider(name, location, truck_id)
                elif choice == "3":
                    # Reassign A Rider's Location
                    id_ = input("Enter Rider's id: > ")
                    location = input("Enter New Route: > ")
                    truck_id = input("Enter Truck id: > ")
                    update_rider(id_, location, truck_id)
                elif choice == "4":
                    get_all_trucks()
                elif choice == "5":
                    get_all_riders()
                elif choice == "6":
                    get_all_orders()
                elif choice == "7":
                    get_all_pending_deliveries()
                elif choice == "8":
                    get_all_completed_deliveries()
                elif choice == "9":
                    product = input("Enter product name: ")
                    quantity = input("Enter quantity: ")
                    cost = input("Enter cost: ")
                    customer_name = input("Enter customer name: ")
                    location = input("Enter location: ")
                    create_order(product, quantity, cost, customer_name, location)
                else:
                    print(f"\033[032m\033[1m ******************INVALID CHOICE******************\033[0m")
        elif choice == "2":
            while True:
                order_fulfilment()
                choice = input("> ")
                if choice == "0":
                    main()
                elif choice == "1":
                    order_id = input("Enter Order id: ")
                    rider_id = input("Enter rider's id: ")
                    create_delivery(order_id, rider_id)
                elif choice == "2":
                    print("Should make an update on an existing delivery")
                elif choice == "3":
                    print("Should delete an existing delivery")
                elif choice == "4":
                    get_all_completed_deliveries()
                elif choice == "5":
                    get_all_pending_deliveries()
                elif choice == "6":
                    product = input("Enter product name: ")
                    quantity = input("Enter quantity: ")
                    cost = input("Enter cost: ")
                    customer_name = input("Enter customer name: ")
                    location = input("Enter location: ")
                    create_order(product, quantity, cost, customer_name, location)
                else:
                    print(f"\033[032m\033[1m ******************INVALID CHOICE******************\033[0m")
        elif choice == "3":
            while True:
                reports()
                choice = input("> ")
                if choice == "0":
                    main()
                else:
                    print(f"\033[032m\033[1m ******************INVALID CHOICE******************\033[0m")
        elif choice == "4":
            product = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            cost = input("Enter cost: ")
            customer_name = input("Enter customer name: ")
            location = input("Enter location: ")
            create_order(product, quantity, cost, customer_name, location)
        else:
            print(f"\033[032m\033[1m ******************INVALID CHOICE******************\033[0m")


def menu():
    print("\033[036m\033[1m******************PLEASE SELECT AN OPTION******************\033[0m")
    print("\033[093m 0. Exit the program \033[0m")
    print("\033[093m 1. Manage Supply Chain \033[0m")
    print("\033[093m 2. Order Fulfilment \033[0m")
    print("\033[093m 3. Reports \033[0m")
    print("\033[093m 4. Create An Order \033[0m")

def manage_supply_chain():
    print("\033[036m\033[1m******************SUPPLY CHAIN MANAAGEMENT******************\033[0m")
    print("\033[093m 0. Go To Main Menu \033[0m")
    print("\033[093m 1. Add Truck To Your Fleet\033[0m")
    print("\033[093m 2. Add A New Rider\033[0m")
    print("\033[093m 3. Reassign A Rider\033[0m")
    print("\033[093m 4. View Your Fleet\033[0m")
    print("\033[093m 5. View All Riders\033[0m")
    print("\033[093m 6. View All Orders\033[0m")
    print("\033[093m 7. View All Pending Deliveries\033[0m")
    print("\033[093m 8. View All Completed Deliveries \033[0m")
    print("\033[093m 9. Create An Order \033[0m")

def order_fulfilment():
    print("\033[036m\033[1m******************ORDER FULFILMENT******************\033[0m")
    print("\033[093m 0. Go To Main Menu \033[0m")
    print("\033[093m 1. Create Delivery \033[0m")
    print("\033[093m 2. Edit Delivery \033[0m")
    print("\033[093m 3. Delete Delivery \033[0m")
    print("\033[093m 4. View Past Deliveries \033[0m")
    print("\033[093m 5. View Pending Deliveries \033[0m")
    print("\033[093m 6. Create An Order \033[0m")
    
def reports():
    print("\033[036m\033[1m******************REPORTS******************\033[0m")
    print("\033[093m 0. Go To Main Menu \033[0m")
    print("\033[093m 1. View All Riders \033[0m")
    print("\033[093m 2. View All Trucks \033[0m")
    print("\033[093m 3. View All Orders \033[0m")
    print("\033[093m 4. View All Deliveries \033[0m")
    print("\033[093m 5. View All Pending Deliveries \033[0m")
    print("\033[093m 6. View All Pending Deliveries By Location\033[0m")
    print("\033[093m 7. View All Pending Deliveries With No Rider Assigned\033[0m")
    print("\033[093m 8. View A Rider's Deliveries \033[0m")
    print("\033[093m 9. View A Rider's Pending Deliveries \033[0m")
    print("\033[093m 10. Create An Order \033[0m")

if __name__ == "__main__":
    main()