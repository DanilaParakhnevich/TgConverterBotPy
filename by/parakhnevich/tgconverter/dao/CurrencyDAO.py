import requests
from by.parakhnevich.tgconverter.dao.DAO import DAO

class CurrencyDAO(DAO):

    headers = {'Accept': 'application/json'}

    def getFullResponse(self):
        return requests.get("https://belarusbank.by/api/kursExchange", self.headers).json()