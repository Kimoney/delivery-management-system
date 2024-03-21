from helpers import (
    exit_program,
    helper_1,
    create_database,
    create_order
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
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
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Create a database")
    print("3. Create a order")


if __name__ == "__main__":
    main()