class Car:
    def __init__(self,year, make, model):
        self.year = year
        self.make = make
        self.model = model
    
    def age(self):
        return (2020-self.year)

myCar = Car(2000,"GM","S10")

print(myCar.age())