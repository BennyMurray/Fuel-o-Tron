import unittest
from RoutePlan import*
from AirportAtlas  import AirportAtlas
from PlaneList import PlaneList
from CurrencyRates import CurrencyList, CurrencyRateList

atlas = AirportAtlas()
planes = PlaneList()
currencyList = CurrencyList()
currencyRates = CurrencyRateList()


class RoutePlanTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.testRoutePlan = Route("DUB", "LON", "ZYA", "HEN", "VOG", "747", "1.02", "1.80", "0.74", "3.54")


    def test_RoutePlanner(self):
        itinerary = ["DUB", "LON", "ZYA", "HEN", "VOG"]
        origin = "DUB"
        homeAirport = "DUB"
        aircraft = "747"
            
        result = self.testRoutePlan.routePlanner(itinerary,origin, homeAirport, aircraft)
        self.assertEqual(('Stage 1: Depart', 'Dublin', 'to', 'London'), result[0]) #First entry on correct list of expected return value
        print (result)

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
