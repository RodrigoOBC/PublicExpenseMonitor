import requests as req

class Deputy:
    def __init__(self, cpf=None, UF=None, party=None, name=None):
        self.cpf = cpf
        self.UF = UF
        self.party = party
        self.name = name
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
        }
        self.url_base = "https://dadosabertos.camara.leg.br/api/v2/deputados"
    
    def check_healf(self):
        response  = req.get(self.url_base, headers=self.headers)
        if response.status_code == 200:
            return {"HealfStatusDeputy": "ok"}
        else:
            response.raise_for_status()

    def get_all_deputy(self):
        url = f"{self.url_base}?itens=250&ordem=ASC&ordenarPor=nome"
        response = req.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    def get_deputy_by_UF(self):
        url = f"{self.url_base}?itens=250&ordem=ASC&ordenarPor=nome&siglaUf={self.UF}"
        response = req.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    
    def get_deputy_by_name(self):
        url = f"{self.url_base}?nome={self.name}&ordem=ASC&ordenarPor=nome"
        response = req.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_id_deputy(self, response):
        deputy_id_name = []
        data = response["dados"]
        for deputy in data:
            deputy_id_name.append({"id": deputy["id"], "name": deputy["nome"]})
        
        return deputy_id_name