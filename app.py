from fastapi import FastAPI
from src.API.Political.deputy import Deputy
from src.API.Expenditures.expenditures import Expenditures
import requests as req
import json

app = FastAPI()

@app.get("/healf")
def check_healf():
    deputy_status = Deputy().check_healf()
    return [deputy_status]

@app.get("/deputy")
def get_all_deputy():
    deputy = Deputy()
    return {"data" : deputy.get_all_deputy()}

@app.get("/deputy/UF={UF}")
def get_deputy_by_UF(UF: str):
    deputy = Deputy(UF=UF)
    return {"data" : deputy.get_deputy_by_UF()}

@app.get("/deputy/name={name}")
def get_deputy_by_name(name: str):
    deputy = Deputy(name=name)
    return {"data" : deputy.get_deputy_by_name()}

@app.get("/expenditures")
def get_deputy_expenditure():
    responses = get_all_deputy()
    expendituresDeputy = []
    for response in responses["data"]["dados"]:
        expenditures = Expenditures(response["id"])
        response_expenditures = expenditures.get_deputy_expenditure()
        expendituresDeputy.append(response_expenditures)
    return {"data" : expendituresDeputy}

@app.get("/expenditures/UF={UF}")
def get_deputy_expenditure_by_UF(UF: str):
    responses = get_deputy_by_UF(UF)
    expendituresDeputy = []
    for response in responses["data"]["dados"]:
        expenditures = Expenditures(response["id"])
        response_expenditures = expenditures.get_deputy_expenditure()
        expendituresDeputy.append(response_expenditures)
    return {"data" : expendituresDeputy}

@app.get("/expenditures/deputyID={id}")
def get_deputy_expenditure_by_UF(deputyID: str):
    expenditures = Expenditures(deputyID)
    response_expenditures = expenditures.get_deputy_expenditure()
    return {"data" : response_expenditures}

@app.get("/expenditures/name={name}")
def get_deputy_expenditure_by_name(name: str):
    responses = get_deputy_by_name(name)
    deputy = Deputy()
    ids = deputy.get_id_deputy(responses["data"])
    expenditures = Expenditures(ids[0]["id"])
    response_expenditures = expenditures.get_deputy_expenditure()

    return {"data" : response_expenditures}