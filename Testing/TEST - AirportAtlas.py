import unittest
from AirportAtlas import AirportAtlas 


class AtlasDistanceTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.known_values = ((53.34, 6.2), (53.34, 6.2))   #####Coordinates of Dublin.
        self.testAtlas = AirportAtlas("airport.csv")

        
    def test_getDistBetween_known_values(self):
        code1 = self.known_values[0]
        code2 = self.known_values[1]
            
        result = self.testAtlas.getDistance(code1, code2)
        self.assertEqual(0, result)  ######Distance fro Dublin to Dublin should be zero

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
