from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from dotenv import load_dotenv
from state import State
import os

load_dotenv()

Base = declarative_base()

class Institution(Base):
    __tablename__ = 'institution'
    
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    CNPJ = Column(String, unique=True, nullable=False)
    State_id = Column(Integer, ForeignKey(State.ID))

    
    def create_table(self, engine):
        Base.metadata.create_all(engine) 
    
    def insert_values(self, session, id, name, cnpj, state_id):
        new_institution = Institution(ID=id, Name=name, CNPJ=cnpj, State_id=state_id)
        session.add(new_institution)
        session.commit()
    
    def delete_values(self, session, id):
        institution_to_delete = session.query(Institution).filter_by(ID=id).first()
        if institution_to_delete:
            session.delete(institution_to_delete)
            session.commit()
    
    def update_values(self, session, id, new_name, new_cnpj, new_state_id):
        institution_to_update = session.query(Institution).filter_by(ID=id).first()
        if institution_to_update:
            institution_to_update.Name = new_name
            institution_to_update.CNPJ = new_cnpj
            institution_to_update.State_id = new_state_id
            session.commit()
    
    def select_all_values(self, session):
        return session.query(Institution).all()

    def select_value_by_id(self, session, id):
        return session.query(Institution).filter_by(ID=id).first()
    
if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get('PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    institution = Institution()
    institution.create_table(conectorDB.engine)
    print(institution.select_all_values(db))