#CREATES A PLANE CLASS
class Plane(object):

    def __init__(self, code,type,units,manufacturer,range):
        self.code = code
        self.type = type
        self.units = units
        self.manufacturer = manufacturer
        self.range = range

    def __str__(self):
        planestr=""
        return "(Code: {}, Type: {}, Units: {}, Manufacturer: {}, Range: {})".format(self.code, self.type, self.units, self.manufacturer, self.range)