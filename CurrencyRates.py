#IMPORT MODULES
from Currency import*

#CREATES A CURRENCYRATES CLASS
class CurrencyRates(object):

    def __init__(self, currency_name, currency_code, to_euro, from_euro):

        self.country_name = currency_name
        self.currency_code = currency_code
        self.to_euro = to_euro
        self.from_euro = from_euro

    def __str__(self):
        currencyRatestr=""
        return "(Currency Name: {}, Exchanged to Euros: {}, Exchanged from Euros: {}, Code: {} )".format(self.country_name, self.to_euro, self.from_euro, self.currency_code)

#CREATES A CURRENCYRATELIST CLASS
class CurrencyRateList:
    currency_fn = "currencyrates.csv"

    def __init__(self, currency_file = currency_fn):
        self.exchangeRates = self.buildExchangeRateDict(currency_file)

    def getExchangeRate(self, code):
        try:
            return self.exchangeRates[code]
        except KeyError:
            return None

    #POPULATES A DICTIONARY OF CURRENCYRATES OBJECTS
    def buildExchangeRateDict(self, filename):
        exchangeRates = {}
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    exchangeRates[row[1]] = CurrencyRates(row[0],row[2], row[3], row[1])

                except KeyError:

                    continue
            return exchangeRates






