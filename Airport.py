#CREATES AIRPORT CLASS
class Airport(object):

    def __init__(self, airport_code, name, country_name, city, latitude, longitude):
        self.code = airport_code
        self.country = country_name
        self.city = city
        self.name = name
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        airportstr=""
        return "{} (Name: {}, {}, {} lat:{} lon:{})".format(self.code, self.name, self.city, self.country, self.latitude, self.longitude)



