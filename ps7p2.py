class Car:
    def __init__(self, make, model, sticker_prc):
        self.make = make
        self.model = model
        self.sticker_prc = sticker_prc

    def dis_price(self):
        return self.sticker_prc * 0.9

C = Car("Kia", "Nero", 35000)
print("Car")
print("Car Make:", C.make)
print("Car Model:", C.model)
print("Sticker price: $%.2f"% C.sticker_prc)
print("Discount Price: $%.2f"% C.dis_price())

class Sport(Car):
    def __init__(self, make, model, sticker_prc):
        super().__init__(make, model, sticker_prc)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"
        self.options_prc = 0

    def add_sport_wheels(self):
        self.sport_wheels = "Y"
        self.options_prc = self.options_prc + 1000

    def add_sport_engine(self):
        self.sport_engine = "Y"
        self.options_prc = self.options_prc + 3000

    def add_sport_interior(self):
        self.sport_interior = "Y"
        self.options_prc = self.options_prc + 2000

    def options_with_prc(self):
        return self.sticker_prc + self.options_prc

S = Sport("Ford", "Mustang", 50000)
print()
print("Sports Car")
print("Car Make:", S.make)
print("Car Model:", S.model)
print("Sticker price: $%.2f"% S.sticker_prc)
print("Discount Price: $%.2f"% S.dis_price())
S.add_sport_wheels()
print("Cost with sport wheels: $%.2f"% S.options_with_prc())
S.add_sport_engine()
print("Cost with sport wheels and sport engine: $%.2f"% S.options_with_prc())
S.add_sport_interior()
print("Cost with sport wheels, sport engine, and sport interior: $%.2f"% S.options_with_prc())