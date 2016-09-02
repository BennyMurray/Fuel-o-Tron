import unittest
from CurrencyRates import CurrencyRateList

class CurrencyListTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.testCurrency = CurrencyRateList("currencyrates.csv")
        self.currency_code_for_Japanese_Yen = "JPY"

        
    def test_getPlane(self):
        code = self.currency_code_for_Japanese_Yen

            
        result = self.testCurrency.getExchangeRate(code).to_euro
        self.assertEqual("127.877", result)  ######exchange rate for Japanese Yen to euro = 127.877

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
