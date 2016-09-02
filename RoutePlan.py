#IMPORT MODULES
from AirportAtlas  import AirportAtlas
from PlaneList import PlaneList
from CurrencyRates import CurrencyList, CurrencyRateList

#CREATE OBJECTS
atlas = AirportAtlas()
planes = PlaneList()
currencyList = CurrencyList()
currencyRates = CurrencyRateList()

#CREATES ROUTE CLASS
class Route(object):
    def __init__(self, origin, city1, city2, city3, city4, plane, exchangeRate_city1, exchangeRate_city2,exchangeRate_city3, exchangeRate_city4):
        self.origin = origin
        self.city1 = city1
        self.city2 = city2
        self.city3 = city3
        self.city4 = city4
        self.plane = plane
        self.exchangeRate_city1 = exchangeRate_city1
        self.exchangeRate_city2 = exchangeRate_city2
        self.exchangeRate_city3 = exchangeRate_city3
        self.exchangeRate_city4 = exchangeRate_city4

    def __str__(self):
        routestr=""
        return "Origin: {} \nDestinations: {}, {}, {}, {}\nAircraft: {}\nExchange-Rates: {}, {}, {}, {}  ".format(self.origin, self.city1.name, self.city2.name, self.city3.name, self.city4.name, self.plane.code, self.exchangeRate_city1, self.exchangeRate_city2, self.exchangeRate_city3, self.exchangeRate_city4)

    #CALCLUATES THE OPTIMUM ROOT
    def routePlanner(self, itinerary, origin, homeAirport, aircraft):

        cost = 0
        actualCost = 0
        failure = 0
        fuelCounter = 0
        currencyUtilised = []

        #CONVERTS FUEL CAPACITY TO METRIC IF REQUIRED
        if len(aircraft) == 3 and aircraft[0] != "F":
            range = int(planes.getPlane(aircraft).range) * 1.609
            fuel = int(planes.getPlane(aircraft).range) * 1.609
        else:
            fuel = int(planes.getPlane(aircraft).range)
            range = int(planes.getPlane(aircraft).range)



         #AT EACH LEG OF JOURNEY, FUNCTION DETERMINES ONE OF THREE OUTCOMES:

          #A. DESTINATION IS OUT OF AIRCRAFT'S RANGE
          #B. AIRCRAFT MUST REFUEL BEFORE PROCEEDING (AND DETERMINE COST BASED ON LOCAL EXCHANGE RATE)
          #C. AIRCRAFT MAY PROCEED WITHOUT REFUELING

        ##########JOURNEY ONE#################
        pointa = atlas.shortestRoute(itinerary, "DUB", homeAirport)
        fuel -= pointa[1]
        if pointa[1] >= range:
            failure_message = "One of the journeys on your itinerary necessitates a flight of approximately", round(pointa[1],2), "km from", atlas.getAirport("DUB").country, "to", atlas.getAirport(pointa[0]).country, "which exceeds the aircraft's maximum flight range of", range, "kilometers. In order to utilise the shortest route, Please recompute your route or select an aircraft with a larger fuel capacity."
            failure += 1
        else:
            stage1 = "Stage 1: Depart",atlas.getAirport(homeAirport).city,"to",atlas.getAirport(pointa[0]).city

        ##########JOURNEY TWO#################
        pointb = atlas.shortestRoute(itinerary, pointa[0], homeAirport)
        if pointb[1] >= range:
            failure_message = "One of the journeys on your itinerary necessitates a flight of approximately", round(pointb[1],2), "km from", atlas.getAirport(pointa[0]).country, "to", atlas.getAirport(pointb[0]).country, "which exceeds the aircraft's maximum flight range of", range, "kilometers. Please recompute your route or select an aircraft with a larger fuel capacity."
            failure += 1

        elif fuel - pointb[1] < 0:
            cost = range - fuel
            actualCost += cost * float(currencyRates.getExchangeRate(currencyList.getCurrency(atlas.getAirport(pointa[0]).country).currency_code).to_euro)
            currencyUtilised.append(" - ")
            currencyUtilised.append(currencyList.getCurrency(atlas.getAirport(pointa[0]).country).currency_name)
            stage2 = "Stage 2: Refuel at",atlas.getAirport(pointa[0]).city,"and proceed to",atlas.getAirport(pointb[0]).city
            fuel = range
            fuel -= pointb[1]
            fuelCounter += cost
        else:
            stage2 = "Stage 2: Depart",atlas.getAirport(pointa[0]).city,"to",atlas.getAirport(pointb[0]).city
            fuel -= pointb[1]

        ##########JOURNEY THREE#################
        pointc = atlas.shortestRoute(itinerary, pointb[0], homeAirport)
        if pointc[1] >= range:
            failure_message = "One of the journeys on your itinerary necessitates a flight of approximately", round(pointc[1],2), "km from", atlas.getAirport(pointb[0]).country, "to", atlas.getAirport(pointc[0]).country, "which exceeds the aircraft's maximum flight range of", range, "kilometers. Please recompute your route or select an aircraft with a larger fuel capacity."
            failure += 1

        elif fuel - pointc[1] < 0:
            cost = range - fuel
            actualCost += cost * float(currencyRates.getExchangeRate(currencyList.getCurrency(atlas.getAirport(pointb[0]).country).currency_code).to_euro)
            currencyUtilised.append(" - ")
            currencyUtilised.append(currencyList.getCurrency(atlas.getAirport(pointb[0]).country).currency_name)
            stage3 = "Stage 3: Refuel at",atlas.getAirport(pointb[0]).city,"and proceed to",atlas.getAirport(pointc[0]).city
            fuel = range
            fuel -= pointc[1]
            fuelCounter += cost
        else:
            fuel -= pointc[1]
            stage3 = "Stage 3: Depart",atlas.getAirport(pointb[0]).city,"to",atlas.getAirport(pointc[0]).city

        ##########JOURNEY FOUR#################
        pointd = atlas.shortestRoute(itinerary, pointc[0], homeAirport)
        if pointd[1] >= range:
            failure_message = "One of the journeys on your itinerary necessitates a flight of approximately", round(pointd[1],2), "km from", atlas.getAirport(pointc[0]).country, "to", atlas.getAirport(pointd[0]).country, "which exceeds the aircraft's maximum flight range of", range, "kilometers. Please recompute your route or select an aircraft with a larger fuel capacity."
            failure += 1

        elif fuel - pointd[1] < 0:
            cost = range - fuel
            actualCost += cost * float(currencyRates.getExchangeRate(currencyList.getCurrency(atlas.getAirport(pointc[0]).country).currency_code).to_euro)
            currencyUtilised.append(" - ")
            currencyUtilised.append(currencyList.getCurrency(atlas.getAirport(pointc[0]).country).currency_name)
            stage4 = "Stage 4: Refuel at",atlas.getAirport(pointc[0]).city,"and proceed to",atlas.getAirport(pointd[0]).city
            fuel = range
            fuel -= pointd[1]
            fuelCounter += cost
        else:
            fuel -= pointd[1]
            stage4 = "Stage 4: Depart",atlas.getAirport(pointc[0]).city,"to",atlas.getAirport(pointd[0]).city
       # pointe = atlas.shortestRoute(itinerary, pointd[0], homeAirport)
            
        ##########RETURN TRIP#################
        itinerary.append(homeAirport)
        pointe = atlas.shortestRoute(itinerary, pointd[0], homeAirport)
        if pointe[1] >= range:
            failure_message =  "One of the journeys on your itinerary necessitates a flight of approximately", round(pointe[1],2), "km from", atlas.getAirport(pointd[0]).country, "to", atlas.getAirport(pointe[0]).country, "which exceeds the aircraft's maximum flight range of", range, "kilometers. Please recompute your route or select an aircraft with a larger fuel capacity."
            failure += 1

        elif fuel - pointe[1] < 0:
            cost = range - fuel
            actualCost += cost * float(currencyRates.getExchangeRate(currencyList.getCurrency(atlas.getAirport(pointd[0]).country).currency_code).to_euro)
            currencyUtilised.append(" - ")
            currencyUtilised.append(currencyList.getCurrency(atlas.getAirport(pointd[0]).country).currency_name)
            stage5 ="Stage 5: Refuel at",atlas.getAirport(pointd[0]).city,"and proceed to",atlas.getAirport(pointe[0]).city
            fuel = range
            fuel -= pointe[1]
            fuelCounter += cost
        else:
            fuel -= pointe[1]
            stage5 = "Stage 5: Depart",atlas.getAirport(pointd[0]).city,"to",atlas.getAirport(homeAirport).city
        
        
        ##########RETURN VALUES#################
        totalDistance = pointa[1] + pointb[1] + pointc[1] + pointd[1] + pointe[1]
        manifest_list = [homeAirport, pointa[0], pointb[0], pointc[0], pointd[0],pointe[0]]
        if failure <= 0:
            finalList = [stage1, stage2, stage3, stage4, stage5, totalDistance, fuelCounter, actualCost, currencyUtilised, manifest_list]
            return finalList
        else:
            finalList = [failure_message]
            return finalList






