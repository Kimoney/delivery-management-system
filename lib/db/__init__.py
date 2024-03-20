from base import Base
from orders import Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CreateDatabase:
    def  __init__(self, db_name):
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        Session =  sessionmaker(bind=self.engine)
        self.session=Session()



if __name__ == '__main__':

    trial = CreateDatabase("trial.db")
    print(f"\033[92m Success!! Database Created.\033[0m")
