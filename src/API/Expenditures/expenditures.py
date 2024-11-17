import requests as req

class Expenditures:
    def __init__(self, id_deputy=None):
        self.id_deputy = id_deputy
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        self.url_base = "https://dadosabertos.camara.leg.br/api/v2/deputados"

    def get_deputy_expenditure(self):
        url = f"{self.url_base}/{self.id_deputy}/despesas?itens=250&ordem=ASC&ordenarPor=ano"
        response = req.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()