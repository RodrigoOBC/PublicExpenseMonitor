from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from conector import Conector
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()


class State(Base):
    __tablename__ = 'state'

    ID = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    UF = Column(String)

    def create_table(self, engine):
        Base.metadata.create_all(engine)

    def insert_values(self, session, id, name, uf):
        new_state = State(ID=id, Name=name, UF=uf)
        session.add(new_state)
        session.commit()

    def delete_values(self, session, id):
        state_to_delete = session.query(State).filter_by(ID=id).first()
        if state_to_delete:
            session.delete(state_to_delete)
            session.commit()

    def update_values(self, session, id, new_name, new_uf):
        state_to_update = session.query(State).filter_by(ID=id).first()
        if state_to_update:
            state_to_update.Name = new_name
            state_to_update.UF = new_uf
            session.commit()

    def select_all_values(self, session):
        return session.query(State).all()

    def select_value_by_id(self, session, id):
        return session.query(State).filter_by(ID=id).first()


if __name__ == "__main__":
    conectorDB = Conector(os.environ.get('USER_DB'), os.environ.get(
        'PASS_DB'), os.environ.get('DB_NAME'))
    db = conectorDB.conect()
    state = State()
    state.create_table(conectorDB.engine)

    estados_brasileiros = [
        {"id": 1, "name": "Acre", "uf": "AC"},
        {"id": 2, "name": "Alagoas", "uf": "AL"},
        {"id": 3, "name": "Amapá", "uf": "AP"},
        {"id": 4, "name": "Amazonas", "uf": "AM"},
        {"id": 5, "name": "Bahia", "uf": "BA"},
        {"id": 6, "name": "Ceará", "uf": "CE"},
        {"id": 7, "name": "Distrito Federal", "uf": "DF"},
        {"id": 8, "name": "Espírito Santo", "uf": "ES"},
        {"id": 9, "name": "Goiás", "uf": "GO"},
        {"id": 10, "name": "Maranhão", "uf": "MA"},
        {"id": 11, "name": "Mato Grosso", "uf": "MT"},
        {"id": 12, "name": "Mato Grosso do Sul", "uf": "MS"},
        {"id": 13, "name": "Minas Gerais", "uf": "MG"},
        {"id": 14, "name": "Pará", "uf": "PA"},
        {"id": 15, "name": "Paraíba", "uf": "PB"},
        {"id": 16, "name": "Paraná", "uf": "PR"},
        {"id": 17, "name": "Pernambuco", "uf": "PE"},
        {"id": 18, "name": "Piauí", "uf": "PI"},
        {"id": 19, "name": "Rio de Janeiro", "uf": "RJ"},
        {"id": 20, "name": "Rio Grande do Norte", "uf": "RN"},
        {"id": 21, "name": "Rio Grande do Sul", "uf": "RS"},
        {"id": 22, "name": "Rondônia", "uf": "RO"},
        {"id": 23, "name": "Roraima", "uf": "RR"},
        {"id": 24, "name": "Santa Catarina", "uf": "SC"},
        {"id": 25, "name": "São Paulo", "uf": "SP"},
        {"id": 26, "name": "Sergipe", "uf": "SE"},
        {"id": 27, "name": "Tocantins", "uf": "TO"},
    ]

    for estado in estados_brasileiros:
        state.insert_values(db, estado["id"], estado["name"], estado["uf"])

    for estado in state.select_all_values(db):
        print(estado.Name, estado.UF)
