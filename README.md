# DELIVERY MANAGEMENT SYSTEM

## Introduction
**Delivery Management System (DMS)** is an efficient delivery management system crucial for businesses to streamline their order fulfilment operations and provide satisfactory service to customers. This project uses Python ORM to optimize the process of managing deliveries for businesses of various scales.


## Features
**Delivery Management System's** efficiency is leveraged from these features:
- **Order Management:** Ability to create, view, edit, and delete orders, including tracking their status.
- **Fleet Management:** Ability to create, view, edit, and delete orders, including tracking their status.
- **Rider Management:** Ability to create, view, edit, and delete riders, including tracking their performance.
- **Delivery Management:** Ability to create, view, and delete delivieries.
- **Reporting:** The functionality offers users convenient ways to analyze and track various aspects of the `Delivery Management System (DMS)`, facilitating informed decision-making and efficient operation management.

## REQUIREMENTS

The following are the system requirements to have the programs running.
1. **Operating System - Linux, Windows & Mac OS**
2. **Python Version 3**

## DEPENDENCIES
- **SQLAlchemy**
- **Tabulate**

## INSTALLATION

- **Clone the repository.**
- **Navigate to the project directory and open in terminal.**

### Using `venv` (recommended for most users)

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```
2.  **Activate the virtual environment:**
    *   On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: You may need to create a `requirements.txt` file by running `pip freeze > requirements.txt` after installing dependencies manually, or simply install `SQLAlchemy` and `Tabulate` directly: `pip install SQLAlchemy tabulate`.*
4.  **Run `python -m lib.seed` to create a test database, and populate it with data.**
5.  **Run `python lib/cli.py` to run `DMS`**

### Using `pipenv` (for developers managing project dependencies)

1.  **Install `pipenv` globally if you haven't already:**
    ```bash
    pip install pipenv
    ```
2.  **Run `pipenv install` to create a virtual environment and install required `Dependencies`.**
3.  **Run `pipenv shell` to activate the virtual environment.**
4.  **Run `python -m lib.seed` to create a test database, and populate it with data.**
5.  **Run `python lib/cli.py` to run `DMS`**

## USAGE

To use the `DMS`, follow these steps:

1.  **Activate the virtual environment:**
    *   If using `venv`:
        *   On macOS and Linux: `source venv/bin/activate`
        *   On Windows: `.\venv\Scripts\activate`
    *   If using `pipenv`: `pipenv shell`
2.  Start the application by executing `python lib/cli.py`.
3.  Follow the on-screen prompts to navigate through the menu options.
4.  Choose the desired functionality (e.g., View Orders, Create Delivery, Add Truck, etc.).
5.  Input data as required and follow the instructions to perform actions.

## Menu Structure

The DMS features a menu-driven interface with the following options:

-   **Manage Supply Chain:** View, add, edit, and delete trucks and riders.
-   **Order Fulfillment:** Create, delete, and view deliveries and orders.
-   **Reports:** Generate various reports to analyze order and delivery data.

For detailed instructions on each menu option, refer to the application's user manual.

## Contributing
Contributions to the `DMS` project are welcome! To contribute, please follow these guidelines:

-   Fork the repository and create a new branch for your feature or bug fix.
-   Implement your changes and ensure that the code adheres to project standards.
-   Submit a pull request detailing the changes made and any relevant information.

## License
This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute the code for personal or commercial purposes.

## Author

**John Kimani M.**
