Проект на языке python
Описание:

def my_function(name):  #печатает приветственное сообщение с именем
    print(f"npивет,{name}")
my_function("Абоба") #пример вызова функции


class Location: #класс представляющий местоположение автомобиля
    def __init__(self, marka, model):
      self.marka = marka #марка
      self.model = model #модель
person1 = Location("Porsche", 911)
print(person1.marka) #выводит марку автомобиля
print(person1.model) #выводит модель автомобиля


class Car(Location): #класс представляющий автомобиль который наследует от класса Location
    def __init__(self, marka, model, years): #марка, модель и год
        super().__init__ (marka, model)
        self.years = years

    def describe(self): #возвращает описание автомобиля
        return f" Я жертва Саши Куралёва, он украл меня на {self.marka} {self.model}. Это произошло в {self.years} году"

car1 = Car("Порш", 911, 2021) #создание экземпляра класса car
print(car1.describe()) #выводит описание car

Сохраните файл и закройте текстовый редактор.
Запустите файл с помощью Python:
Выводит:
npивет, Абоба

Porsche
911

Я жертва Саши Куралёва, он украл меня на Порш 911. Это произошло в 2021 году
