#IMPORT MODULES
from Plane import Plane
import os,csv

#CREATES PLANE LIST CLASS
class PlaneList:
    aircraft_fn = "aircraft.csv"

    def __init__(self, aircraft_file = aircraft_fn):
        self.planes = self.buildPlaneDict(aircraft_file)

    def getPlane(self, code):
        try:
            return self.planes[code]
        except KeyError:
            return None

    #BUILDS A DICTIONARY OF PLANE OBJECTS
    def buildPlaneDict(self, filename):
        planes = {}
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    planes[row[0]] = Plane(row[0],row[1], row[2], row[3], row[4])

                except KeyError:

                    continue
            return planes
