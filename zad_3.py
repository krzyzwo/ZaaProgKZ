class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.area}, {self.rooms}, {self.price}, {self.address}"


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.plot = plot

    def __str__(self):
        return f"{self.area}, {self.rooms}, {self.price}, {self.address}, {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        self.floor = floor

    def __str__(self):
        return f"{self.area}, {self.rooms}, {self.price}, {self.address}, {self.floor}"


Dom = House("80m2", 4, "200000zł", "Katowice", 120)
Mieszkanie = Flat("24m2", 2, "80000zł", "Katowice", 4)
print(Dom)
print(Mieszkanie)
