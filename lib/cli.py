from helpers import (
    exit_program,
    create_order,
    add_truck,
    add_rider,
    create_delivery,
    get_all_orders,
    get_all_trucks,
    get_all_riders,
    get_all_completed_deliveries
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            name = input("Enter rider's name: ")
            location = input("Enter rider's route location: ")
            truck_id = input("Enter rider's truck id: ")
            add_rider(name, location, truck_id)
        elif choice == "2":
          order_id = input("Enter Order id: ")
          rider_id = input("Enter rider's id: ")
          create_delivery(order_id, rider_id)
        elif choice == "3":
            product = input("Enter product name: ")
            quantity = input("Enter quantity: ")
            cost = input("Enter cost: ")
            customer_name = input("Enter customer name: ")
            location = input("Enter location: ")
            create_order(product, quantity, cost, customer_name, location)
        elif choice == "4":
            reg_no = input("Enter Truck's Registration Number: >")
            truck_capacity = input("Enter Truck's Load Capacity: >")
            model = input("Enter Truck's model: >")
            add_truck(reg_no, truck_capacity, model)
        elif choice == "5":
            get_all_orders()
        elif choice == "6":
            get_all_trucks()
        elif choice == "7":
            get_all_riders()
        elif choice == "8":
            get_all_completed_deliveries()
        else:
            print("Invalid choice")


def menu():
    print("\033[036m Please select an option:\033[0m")
    print("\033[093m 0. Exit the program \033[0m")
    print("\033[093m 1. Add A Rider \033[0m")
    print("\033[093m 2. Create Delivery \033[0m")
    print("\033[093m 3. Create An Order \033[0m")
    print("\033[093m 4. Add Truck To Your Fleet \033[0m")
    print("\033[093m 5. View All Orders \033[0m")
    print("\033[093m 6. View Your Fleet \033[0m")
    print("\033[093m 7. View All Riders \033[0m")
    print("\033[093m 8. View All Completed Deliveries \033[0m")
    print("\033[093m 9. View All Pending Deliveries \033[0m")

if __name__ == "__main__":
    main()