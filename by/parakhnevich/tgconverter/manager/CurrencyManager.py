from by.parakhnevich.tgconverter.dao.CurrencyDAO import CurrencyDAO
from by.parakhnevich.tgconverter.model.CurrencyEnum import CurrencyEnum


class CurrencyManager:
    currencyDAO = CurrencyDAO()

    def translate(self, from_currency_enum, to_currency_enum, value):
        response = self.currencyDAO.getFullResponse()
        from_coefficient = 1 if from_currency_enum.value is CurrencyEnum.BYN.value else float(
            response[0].get('{0}{1}'.format(from_currency_enum.value, '_out')))
        if from_currency_enum.value is CurrencyEnum.RUB.value: from_coefficient *= 10

        to_coefficient = 1 if to_currency_enum.value is CurrencyEnum.BYN.value else float(
            response[0].get('{0}{1}'.format(to_currency_enum.value, '_out')))
        if to_currency_enum.value is CurrencyEnum.RUB.value: to_coefficient *= 10

        return (from_coefficient / to_coefficient) * value