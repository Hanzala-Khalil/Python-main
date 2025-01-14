# Operator Overloading

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age


roger = Dog('Roger' , 10)
syd = Dog('Syd' , 9)

print(roger - syd)