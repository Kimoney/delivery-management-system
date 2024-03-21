from helpers import (
    exit_program,
    create_database,
    create_order,
    add_truck
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            pass
        elif choice == "2":
            db_name = input("Enter database name: ")
            create_database(db_name)
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
        else:
            print("Invalid choice")


def menu():
    print("\033[036m Please select an option:\033[0m")
    print("\033[093m 0. Exit the program \033[0m")
    print("\033[093m 1. Empty \033[0m")
    print("\033[093m 2. Create A Database \033[0m")
    print("\033[093m 3. Create An Order \033[0m")
    print("\033[093m 4. Add Truck To Your Fleet \033[0m")


if __name__ == "__main__":
    main()