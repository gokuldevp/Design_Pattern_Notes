"""
The Factory Method pattern is another creational design pattern. It provides an interface for creating objects 
in a superclass but allows subclasses to alter the type of objects that will be created. This pattern is useful
when you want to delegate the instantiation logic to subclasses.

Concept Explanation:
1. Creator: Declares the factory method, which returns an object of type Product. It may also define a default implementation.
2. Concrete Creator: Overrides the factory method to return an instance of a ConcreteProduct.
3. Product: Declares an interface for objects the factory method creates.
4. Concrete Product: Implements the Product interface.

Structure:
Here’s a basic UML diagram to illustrate the structure:

          +-------------------+           +-------------------+
          | Creator           |<----------| Client            |
          |-------------------|           +-------------------+
          | + factoryMethod() |                    
          | + someOperation() |<-----+     
          +-------------------+      |     
                 ^                    | uses
                 |                    |
          +-------------------+       |         
          | ConcreteCreator   |       |         
          |-------------------|       |       
          | + factoryMethod() |       |        
          +-------------------+       |     
                 ^                    |      
                 |                    |
          +-------------------+       |
          | Product           |       |
          +-------------------+       |
          | + operation()     |<------+
          +-------------------+
                 ^
                 |
          +-------------------+
          | ConcreteProduct   |
          +-------------------+
          | + operation()     |
          +-------------------+

"""

# Example Code:
# Here’s a practical example in Python to illustrate the Factory Method pattern:

# Product Interface
class Pet:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def speak(self):
        raise NotImplementedError

# Concrete Products
class Dog(Pet):
    def speak(self):
        return f"woof! I'm {self.name}, a {self.age}-year-old {self.breed}."

class Cat(Pet):
    def speak(self):
        return f"meow! I'm {self.name}, a {self.age}-year-old {self.breed}."

# Creator
class PetFactory:
    def get_pet(self):
        raise NotImplementedError

    def display_pet(self):
        pet = self.get_pet()
        print(f"The pet says: {pet.speak()}")

# Concrete Creators
class DogFactory(PetFactory):
    def get_pet(self):
        return Dog("Jimmy", "Golden Retriever", 2)

class CatFactory(PetFactory):
    def get_pet(self):
        return Cat("Tom", "Persian", 3)

# Client Code
dog_factory = DogFactory()
cat_factory = CatFactory()

dog_factory.display_pet()  # Output: The pet says: woof! I'm Jimmy, a 2-year-old Golden Retriever.
cat_factory.display_pet()  # Output: The pet says: meow! I'm Tom, a 3-year-old Persian.

# The Factory pattern is a design pattern that focuses on creating objects. It encapsulates the object creation process, 
# allowing the system to decide which class to instantiate at runtime. This pattern is particularly useful when the type
# of objects needed is not known until runtime or when the system needs to handle multiple types of objects.

# In simpler terms, the Factory pattern acts like a factory that produces different products (objects) based on the requirements
# at the time. This makes your code more flexible and easier to maintain.

class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "woof!"
    
class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Meow!"
    
def get_pet(pet='dog'):
    pets = {"dog":Dog("Jimmy"), "cat": Cat("Tom")}
    return pets.get(pet, None)

d = get_pet()
c = get_pet('cat')

print(d.speak())
print(c.speak())


###################### OR

class Pet:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return self.sound

def get_pet(pet_type='dog'):
    pets = {
        "dog": Pet("Jimmy", "woof!"),
        "cat": Pet("Tom", "Meow!")
    }
    return pets.get(pet_type, Pet("Unknown", "Silent"))

d = get_pet()
c = get_pet('cat')

print(d.speak())  # Output: woof!
print(c.speak())  # Output: Meow!

######################### in depth



