from helpers import (
    exit_program,
    helper_1,
    create_database
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
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Create a database")


if __name__ == "__main__":
    main()