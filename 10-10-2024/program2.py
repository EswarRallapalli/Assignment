""".Define an abstract class Animal with an abstract method make_sound().
 Then, create three classes that inherit from Animal:

Dog with the sound "Woof".
Cat with the sound "Meow".
Cow with the sound "Moo".
Create a function play_sound(animal) that takes an object of type Animal and calls its make_sound() method.

"""
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Dog: woof")
class Cat(Animal):
    def make_sound(self):
        print( "Cat : Meow")
        
class Cow(Animal):
    def make_sound(self):
        print("Cow : moo")
def play_sound(animal):
    if isinstance(animal,Animal):
        print(animal.make_sound())
dog=Dog()
cat=Cat()
cow=Cow()
play_sound(dog)
play_sound(cat)
play_sound(cow)