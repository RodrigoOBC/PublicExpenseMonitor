from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class PoliticalParty(Base):
    __tablename__ = 'political_party'
    
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Initials = Column(String)

    def create_table(self, engine):
        Base.metadata.create_all(engine)
    
    def insert_values(self, session, id, name, initials):
        new_party = PoliticalParty(ID=id, Name=name, Initials=initials)
        session.add(new_party)
        session.commit()
    
    def delete_values(self, session, id):
        party_to_delete = session.query(PoliticalParty).filter_by(ID=id).first()
        if party_to_delete:
            session.delete(party_to_delete)
            session.commit()
    
    def update_values(self, session, id, new_name, new_initials):
        party_to_update = session.query(PoliticalParty).filter_by(ID=id).first()
        if party_to_update:
            party_to_update.Name = new_name
            party_to_update.Initials = new_initials
            session.commit()
    
    def select_all_values(self, session):
        return session.query(PoliticalParty).all()
    
    def select_value_by_id(self, session, id):
        return session.query(PoliticalParty).filter_by(ID=id).first()
    
if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get('PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    party = PoliticalParty()
    party.create_table(conectorDB.engine)
    party.insert_values(db, 13, 'PT', 'PT')
    party.insert_values(db, 45, 'PSDB', 'PSDB')
    party.insert_values(db, 50, 'PSOL', 'PSOL')
    party.insert_values(db, 18, 'REDE', 'REDE')
    party.insert_values(db, 30, 'NOVO', 'NOVO')
    print(party.select_value_by_id(db,30).Name)
