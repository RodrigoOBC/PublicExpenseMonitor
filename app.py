from fastapi import FastAPI
from src.API.Political.deputy import Deputy
import requests as req

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/deputy")
def get_all_deputy():
    deputy = Deputy()
    return deputy.get_all_deputy()

@app.get("/deputy/UF={UF}")
def get_deputy_by_UF(UF: str):
    deputy = Deputy(UF=UF)
    return deputy.get_deputy_by_UF()

@app.get("/deputy/name={name}")
def get_deputy_by_name(name: str):
    deputy = Deputy(name=name)
    return deputy.get_deputy_by_name()

@app.get("/expenditures")
def get_deputy_expenditure():
    responses = get_all_deputy()
    return responses