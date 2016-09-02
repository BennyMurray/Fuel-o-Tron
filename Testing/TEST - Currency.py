import unittest
from Currency import CurrencyList

class CurrencyListTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.testCurrency = CurrencyList("countrycurrency.csv")
        self.name_of_country = "Georgia"

        
    def test_RoutePlanner(self):
        country = self.name_of_country

            
        result = self.testCurrency.getCurrency(country).currency_code
        self.assertEqual("GEL", result) #GEL is the currency code for the Georgian Lari

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
