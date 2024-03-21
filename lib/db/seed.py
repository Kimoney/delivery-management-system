from . import delivery_management_system
from datetime import datetime

DMS = delivery_management_system.DeliveryManagementSystem

# Create DataBase
    
dms_db = DMS("dms.db")
print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")

dms_db.create_order("Laptop", 5, 2500, "Kimani", "Nairobi")
print(f"\033[92m Success!! Order Created at {datetime.now()} \033[0m")
# dms_db.add_truck("KDA 969K", 2500, "Mitsubishi FH")
# print(f"\033[92m Success!! Truck Added at {datetime.now()} \033[0m")   