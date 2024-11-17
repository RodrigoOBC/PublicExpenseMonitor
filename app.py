from fastapi import FastAPI
from src.API.Political.deputy import Deputy
from src.API.Expenditures.expenditures import Expenditures
import requests as req
import json

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

@app.get("/expenditures/UF={UF}")
def get_deputy_expenditure_by_UF(UF: str):
    responses = get_deputy_by_UF(UF)
    return responses

@app.get("/expenditures/name={name}")
def get_deputy_expenditure_by_name(name: str):
    responses = get_deputy_by_name(name)
    deputy = Deputy()
    ids = deputy.get_id_deputy(responses)
    expenditures = Expenditures(ids[0]["id"])
    response_expenditures = expenditures.get_deputy_expenditure()

    return response_expenditures