#IMPORT MODULES
import os,csv
from math import radians, cos, sin, asin, sqrt
from Airport import Airport



#CREATES AIRPORT ATLAS CLASS
class AirportAtlas:
    airport_fn = "airport.csv"

    def __init__(self, airport_file = airport_fn):
        self.airports = self.buildAirportDict(airport_file)

    def getAirport(self, airport_code):
        try:
            return self.airports[airport_code.upper()]
        except KeyError:
            return None

    #POPULATES A DICTIONAR OF AIRPORT OBJECTS
    def buildAirportDict(self, filename):
        airports = {}
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            csvfilelines = csv.reader(f)
            for row in csvfilelines:
                try:
                    airports[row[4]] = Airport(row[4], row[1], row[3],row[2], float(row[6]), float(row[7]))
                except KeyError:
                    continue
            return airports

    #CALCULATES DISTANCE BETWEEN TWO POINTS
    def getDistance(self, code1,code2):
            lat1 = code1[0]
            lon1 = code1[1]
            lat2 = code2[0]
            lon2 = code2[1]
            lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
            c = 2 * asin(sqrt(a))
            r = 6371
            return c * r
            return distance

    #CALCULATES THE SHORTEST PATH
    def shortestRoute(self, itinerary, origin, homeAirport):

        if len(itinerary) == 1:
            finalPath = self.getDistance((self.getAirport(origin).latitude,self.getAirport(origin).longitude),
                        (self.getAirport(homeAirport).latitude,self.getAirport(homeAirport).longitude))
        else:
            self.itinerary = itinerary
            self.origin = origin
            self.newdict = {}
            self.newlist = []
            for a in itinerary:
                for b in itinerary:
                    distance = self.getDistance((self.getAirport(origin).latitude,self.getAirport(origin).longitude),
                            (self.getAirport(b).latitude,self.getAirport(b).longitude))
                    self.newlist.append(distance)
                    self.newlist.sort()
                    self.newdict[distance] = b
            self.newlist[:] = (value for value in self.newlist if value != 0.0)
            shortestPath = (self.newdict[self.newlist[1]], self.newlist[1])
            if origin in itinerary:
                itinerary.remove(origin)
            return shortestPath






