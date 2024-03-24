from .db import delivery_management_system
from datetime import datetime

DMS = delivery_management_system.DeliveryManagementSystem

# Create DataBase
    
dms_db = DMS("dms.db")
print(f"\033[92m Success!! Database Created at {datetime.now()} \033[0m")


# Create Orders

dms_db.create_order("Dell Laptop", 100, 600000, "Moringa School", "Nakuru")
dms_db.create_order("Notebook", 200, 25000, "Masomo Bookshop", "Kisumu")
dms_db.create_order("Macbook Pro", 10, 2500, "DMS-Kenya", "Nairobi")
dms_db.create_order("Keyboard", 200, 400000, "Pwani University", "Mombasa")
dms_db.create_order("Mouse", 5, 2500, "Starlink Cyber", "Nakuru")
dms_db.create_order("Office Desk", 1, 2500, "John Doe", "Eldoret")
dms_db.create_order("Office Chair", 5, 2500, "Nelson Korir", "Eldoret")
dms_db.create_order("HP Monitor", 5, 150000, "John Kimani", "Nairobi")
dms_db.create_order("Mouse", 10, 5000, "The One Cyber", "Mombasa")
dms_db.create_order("Laptop Stand", 5, 25000, "John Kimani", "Nairobi")
dms_db.create_order("1TB SSD", 5, 90000, "Jane Doe", "Kisumu")
dms_db.create_order("Diaries", 5, 2500, "Starlink Cyber", "Nakuru")
dms_db.create_order("Graphics Card", 5, 2500, "Eliud Kipchoge", "Eldoret")
dms_db.create_order("Printer", 5, 2500, "Kimutai Joe", "Eldoret")
dms_db.create_order("Printing Papers", 5, 2500, "Kimani", "Kisumu")
dms_db.create_order("Sticky Notes", 5, 2500, "Wadau Bookstore", "Nairobi")
dms_db.create_order("Envelopes", 5, 2500, "Saida Bookshop", "Mombasa")
dms_db.create_order("16GB RAM", 5, 2500, "Kaizen Laptop Repairs", "Nairobi")
dms_db.create_order("Air Pods", 5, 2500, "Halima Mpole", "Mombasa")
dms_db.create_order("Macbook Pro", 5, 2500, "Abdala Tajiri", "Mombasa")
dms_db.create_order("Type-C Cable", 5, 2500, "Kimani", "Nairobi")
print(f"\033[93m Success!! Test Orders Created at {datetime.now()}\033[0m")

#  Create Trucks

dms_db.add_truck("KBA 969K", 4000, "Mitsubishi Fuso Canter")
dms_db.add_truck("KDM 320A", 3000, "Toyota Dyna")
dms_db.add_truck("KCN 919C", 4000, "Mitsubishi FH")
dms_db.add_truck("KDC 103Y", 3000, "Toyota Dyna")
dms_db.add_truck("KCA 421Q", 3000, "Toyota Dyna")
dms_db.add_truck("KDN 874W", 4000, "Mitsubishi Fuso Canter")
dms_db.add_truck("KDM 034K", 10000, "Mitsubishi FH")
dms_db.add_truck("KCY 256P", 10000, "Isuzu FRR")
dms_db.add_truck("KDA 562G", 3000, "Toyota Dyna")
print(f"\033[93m Success!! Test Trucks Created at {datetime.now()}\033[0m")   

# Create Riders

dms_db.add_rider("John Kimani", "Nairobi", 1)
dms_db.add_rider("Janet Akinyi", "Kisumu", 2)
dms_db.add_rider("Suleiman Karim", "Mombasa", 3)
dms_db.add_rider("Jane Chep", "Eldoret", 4)
dms_db.add_rider("Kangethe Kamau", "Nakuru", 5)
print(f"\033[93m Success!! Test Riders Created at {datetime.now()}\033[0m")

# Create Deliveries

dms_db.create_delivery(2,2)
dms_db.create_delivery(3,1)
dms_db.create_delivery(3,3)
dms_db.create_delivery(5,5)
dms_db.create_delivery(7,4)
dms_db.create_delivery(21,1)
dms_db.create_delivery(20,3)
dms_db.create_delivery(16,1)
dms_db.create_delivery(15,2)
dms_db.create_delivery(19,3)
dms_db.create_delivery(13, 4)
print(f"\033[93m Success!! Test Deliveries Created at {datetime.now()}\033[0m")