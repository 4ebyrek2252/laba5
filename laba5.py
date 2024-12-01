# def my_function(name):
#     print(f"npивет,{name}")
# my_function("Абоба")


class Location:
    def __init__(self, marka, model):
      self.marka = marka
      self.model = model
person1 = Location("Porsche", 911)
print(person1.marka)
print(person1.model)


class Car(Location):
    def __init__(self, marka, model, years):
        super().__init__ (marka, model)
        self.years = years

    def describe(self):
        return f" Я жертва Саши Куралёва, он украл меня на {self.marka} {self.model}. Это произошло в {self.years} году"

car1 = Car("Порш", 911, 2021)
print(car1.describe())