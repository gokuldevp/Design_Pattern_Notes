"""
# The Abstract Factory pattern is a creational design pattern that provides an interface for creating families
# of related or dependent objects without specifying their concrete classes. This pattern is especially useful
# when the system needs to be independent of how its objects are created, composed, and represented.

Concept Explanation:

1. Abstract Factory: Declares an interface for operations that create abstract product objects.
2. Concrete Factory: Implements the operations to create concrete product objects.
3. Abstract Product: Declares an interface for a type of product object.
4. Concrete Product: Implements the Abstract Product interface.
5. Client: Uses only interfaces declared by Abstract Factory and Abstract Product classes.

Structure:
Here's a basic UML diagram to illustrate the structure:

          +-------------------+           +-------------------+
          | AbstractFactory   |<----------| Client            |
          |-------------------|           +-------------------+
          | + createProductA()|                    
          | + createProductB()|<-----+     
          +-------------------+      |     
                 ^                    | uses
                 |                    |
          +-------------------+       |         
          | ConcreteFactory1  |       |         
          |-------------------|       |       
          | + createProductA()|       |        
          | + createProductB()|       |     
          +-------------------+       |      
                 ^                    | uses
                 |                    |
          +-------------------+       |           
          | ConcreteFactory2  |       |      
          |-------------------|       |      
          | + createProductA()|       |    
          | + createProductB()|       |  
          +-------------------+       |  
                 ^                    |
                 |                    |
          +-------------------+       |
          | AbstractProductA  |       |
          +-------------------+       |
          | + methodA()       |<------+
          +-------------------+
                 ^
                 |
          +-------------------+
          | ConcreteProductA1 |
          +-------------------+
          | + methodA()       |
          +-------------------+
"""

# Example Code:
# Here’s a practical example in Python to illustrate the Abstract Factory pattern:

# Abstract Factory
class PetFactory:
    def create_dog(self):
        raise NotImplementedError
    
    def create_cat(self):
        raise NotImplementedError

# Concrete Factories
class FriendlyPetFactory(PetFactory):
    def create_dog(self):
        return FriendlyDog("Jimmy", "Golden Retriever", 2)

    def create_cat(self):
        return FriendlyCat("Tom", "Persian", 3)

class GuardPetFactory(PetFactory):
    def create_dog(self):
        return GuardDog("Rex", "German Shepherd", 4)

    def create_cat(self):
        return GuardCat("Whiskers", "Siamese", 5)

# Abstract Products
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        raise NotImplementedError

class Cat:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        raise NotImplementedError

# Concrete Products
class FriendlyDog(Dog):
    def speak(self):
        return f"woof, I love you! I'm {self.name}, a {self.age}-year-old {self.breed}."

class GuardDog(Dog):
    def speak(self):
        return f"woof, stay back! I'm {self.name}, a {self.age}-year-old {self.breed}."

class FriendlyCat(Cat):
    def speak(self):
        return f"meow, purr. I'm {self.name}, a {self.age}-year-old {self.breed}."

class GuardCat(Cat):
    def speak(self):
        return f"meow, beware! I'm {self.name}, a {self.age}-year-old {self.breed}."

# Client Code
def get_pet(factory):
    dog = factory.create_dog()
    cat = factory.create_cat()
    return dog, cat

# Usage
friendly_factory = FriendlyPetFactory()
guard_factory = GuardPetFactory()

friendly_dog, friendly_cat = get_pet(friendly_factory)
guard_dog, guard_cat = get_pet(guard_factory)

print(friendly_dog.speak())  # Output: woof, I love you! I'm Jimmy, a 2-year-old Golden Retriever.
print(friendly_cat.speak())  # Output: meow, purr. I'm Tom, a 3-year-old Persian.
print(guard_dog.speak())     # Output: woof, stay back! I'm Rex, a 4-year-old German Shepherd.
print(guard_cat.speak())     # Output: meow, beware! I'm Whiskers, a 5-year-old Siamese.

