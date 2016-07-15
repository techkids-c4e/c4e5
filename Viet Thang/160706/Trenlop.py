##class Dog:
##    def __init__(self, name, age):
##        self.itname = name
##        self.itage = age
##
##    def bark(self):
##        print("Gau Gau")
##lulu = Dog("lulu","5")
##lulu.bark()

manufacturer = "Samsung"

class Person:
    def print(self):
        print("Name:", self.name)
        print("Age", self.age)

    def __init__(self, n, a):
        self.name = n
        self.age = a

class Car:
    def __init__(self, manufacturer, year):
        self.manufacturer = manufacturer
        self.year = year
    def print(self):
        print("manufacturer: ",self.manufacturer)
        print("year: ",self.year)

##p = Person("Ha", 18)
##p.print()
##
##print("-----------------")
##
##p2 = Person("Hiep", 30)
##p2.print()
##
##c1 = Car("Toyota", "1999")
##c1.print()
##
##c2 = Car("Honda", "2000")
##c2.print()
        
person_list = {
    Person("Ha", 18),
    Person("Ly", 20),
    Person("Giang", 25)
    }

for person in person_list:
    person.print()
