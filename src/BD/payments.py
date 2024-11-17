from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from dotenv import load_dotenv
from state import State
import os

load_dotenv()

Base = declarative_base()

class PaymentsType(Base):
    __tablename__ = 'payments'
    
    ID = Column(Integer, primary_key=True, index=True)
    Type_name = Column(String)

    def create_table(self, engine):
        Base.metadata.create_all(engine)
    
    def insert_values(self, session, id, type_name):
        new_payment = PaymentsType(ID=id, Type_name=type_name)
        session.add(new_payment)
        session.commit()
    
    def delete_values(self, session, id):
        payment_to_delete = session.query(PaymentsType).filter_by(ID=id).first()
        if payment_to_delete:
            session.delete(payment_to_delete)
            session.commit()
    
    def update_values(self, session, id, new_type_name):
        payment_to_update = session.query(PaymentsType).filter_by(ID=id).first()
        if payment_to_update:
            payment_to_update.Type_name = new_type_name
            session.commit()
    
    def select_all_values(self, session):
        return session.query(PaymentsType).all()

    def select_value_by_id(self, session, id):
        return session.query(PaymentsType).filter_by(ID=id).first()
    
if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get('PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    payment = PaymentsType()
    payment.create_table(conectorDB.engine)


    
    