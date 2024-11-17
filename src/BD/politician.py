from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from political_paty import PoliticalParty
from position import Position
from state import State
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class Politician(Base):
    __tablename__ = 'politician'
    
    ID = Column(Integer, primary_key=True, index=True)
    PoliticalParty_id = Column(Integer, ForeignKey(PoliticalParty.ID))
    Position_id = Column(Integer, ForeignKey(Position.ID))
    UF_id = Column(Integer, ForeignKey(State.ID))
    CPF = Column(Integer, unique=True, nullable=False)

    def create_table(self, engine):
        Base.metadata.create_all(engine)

    def insert_values(self, session, id, political_party_id, position_id, uf_id, cpf):
        new_politician = Politician(ID=id, PoliticalParty_id=political_party_id, Position_id=position_id, UF_id=uf_id, CPF=cpf)
        session.add(new_politician)
        session.commit()
    
    def delete_values(self, session, id):
        politician_to_delete = session.query(Politician).filter_by(ID=id).first()
        if politician_to_delete:
            session.delete(politician_to_delete)
            session.commit()
    
    def update_values(self, session, id, new_political_party_id, new_position_id, new_uf_id, new_cpf):
        politician_to_update = session.query(Politician).filter_by(ID=id).first()
        if politician_to_update:
            politician_to_update.PoliticalParty_id = new_political_party_id
            politician_to_update.Position_id = new_position_id
            politician_to_update.UF_id = new_uf_id
            politician_to_update.CPF = new_cpf
            session.commit()
    
    def select_all_values(self, session):
        return session.query(Politician).all()

    def select_value_by_id(self, session, id):
        return session.query(Politician).filter_by(ID=id).first()
    
if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get('PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    politician = Politician()
    politician.create_table(conectorDB.engine)
    # politician.insert_values(db, 1, 13, 1, 1, '12345678901')
    # politician.insert_values(db, 2, 45, 2, 2, '12345678902')
    # politician.insert_values(db, 3, 50, 3, 3, '12345678903')
    # politician.insert_values(db, 4, 18, 4, 4, '12345678904')
    # politician.insert_values(db, 5, 30, 5, 5, '12345678905')
    # print(politician.select_value_by_id(db,5).CPF)
    # print(politician.select_value_by_id(db,5).PoliticalParty_id)
    # print(politician.select_value_by_id(db,5).Position_id)
    # print(politician.select_value_by_id(db,5).UF_id)