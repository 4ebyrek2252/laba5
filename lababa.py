def my_function(name):  #печатает приветственное сообщение с именем
    print(f"npивет,{name}")
my_function("Абоба") #пример вызова функции
class Fruit:
    def __init__(self, name='Неизвестный фрукт', quantity=None):
      self.name = name
      self.quantity = quantity
apple = Fruit("яблоки", 13)
print(apple.name)
print(apple.quantity)
class Ves(Fruit):
    def __init__(self, name='Неизвестный фрукт', quantity=None, weight_kg=None):
        super().__init__ (name, quantity)
        self.weight_kg = weight_kg
    def describe(self):
        return f" Красная шапочка шла по лесу и нашла {self.name} в количестве {self.quantity} штук. Теперь её корзинка весит {self.weight_kg} кг"
korzinka = Ves("Яблоки", 13, 1)
print(korzinka.describe())
