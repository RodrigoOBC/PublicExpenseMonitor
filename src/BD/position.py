from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()

class Position(Base):
    __tablename__ = 'position'
    
    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)

    def create_table(self, engine):
        Base.metadata.create_all(engine)

    def insert_values(self, session, id, name):
        new_cargo = Position(ID=id, Name=name)
        session.add(new_cargo)
        session.commit()

    def delete_values(self, session, id):
        cargo_to_delete = session.query(Position).filter_by(ID=id).first()
        if cargo_to_delete:
            session.delete(cargo_to_delete)
            session.commit()

    def update_values(self, session, id, new_name):
        cargo_to_update = session.query(Position).filter_by(ID=id).first()
        if cargo_to_update:
            cargo_to_update.Name = new_name
            session.commit()
    
    def select_all_values(self, session):
        return session.query(Position).all()
    
    def select_value_by_id(self, session, id):
        return session.query(Position).filter_by(ID=id).first()

if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get('PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    position = Position()
    # position.create_table(conectorDB.engine)
    # position.insert_values(db, 1, 'DEPUTADO')
    # position.insert_values(db, 2, 'SENADOR')
    # position.insert_values(db, 3, 'STF')
    # position.insert_values(db, 4, 'MINISTRO')
    # position.insert_values(db, 5, 'PRESDIENTE')
    # print(position.select_value_by_id(db,2).Name)

