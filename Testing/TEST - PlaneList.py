import unittest
from PlaneList import PlaneList

class PlaneListTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.testPlane = PlaneList("aircraft.csv")
        self.seven_four_seven = "747"

        
    def test_getPlane(self):
        code = self.seven_four_seven

            
        result = self.testPlane.getPlane(code).range
        self.assertEqual("9800", result)  ######range of 747 is 9800 kilometers

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()
