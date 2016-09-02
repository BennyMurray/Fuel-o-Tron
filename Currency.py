#IMPORT MODULES
import os,csv

#CREATE CURRENCY CLASS
class Currency(object):

    def __init__(self, country_name, currency_name, currency_code):
        self.country_name = country_name
        self.currency_name = currency_name
        self.currency_code = currency_code

    def __str__(self):
        currencystr=""
        return "(Country: {}, Currency: {}, Currency Code: {})".format(self.country_name, self.currency_name, self.currency_code)

#CREATE CURRENCY LIST CLASS
class CurrencyList:
    currency_fn = "countrycurrency.csv"

    def __init__(self, currency_file = currency_fn):
        self.currencies = self.buildCurrencyDict(currency_file)

    def getCurrency(self, country):
        try:
            return self.currencies[country]
        except KeyError:
            return None

    #POPULATES A DICTIONARY OF CURRENCY OBJECTS
    def buildCurrencyDict(self, filename):
        currencies = {}
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    currencies[row[0]] = Currency(row[0],row[17],  row[14])

                except KeyError:

                    continue
            return currencies



