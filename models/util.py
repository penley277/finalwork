class Time(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getYear(self):
        return  self.year

    def getMonth(self):
        return  self.month

    def getDay(self):
        return self.day

    def setYear(self, year):
        self.year = year

    def setMonth(self, month):
        self.month = month

    def setDay(self, day):
        self.day = day