"""
# Builder Pattern
It helps to construct complex objects step by step by using a series of methods or steps in a consistent manner. 
This pattern is useful when you need to create an object with many optional parameters, as it provides a clear 
and readable way to build such objects without ending up with a constructor with numerous parameters.

How Builder Pattern Works:
1. Builder Interface: Defines the process to create parts of the Product object.
2. Concrete Builder: Implements the Builder interface and constructs and assembles parts of the product.
3. Director: Constructs an object using the Builder interface.
4. Product: The final object that is being built.

Use Cases of Builder Pattern:
1. Complex Object Construction: When an object has multiple fields, especially with many optional parameters. 
   For example, consider building a house with various optional features like a swimming pool, garage, garden, etc.
2. Immutable Objects: When working with immutable objects where you can't modify the object after it's created. 
   The builder pattern allows step-by-step configuration before the object creation.
3. Configuration Objects: Useful for creating complex configuration objects. For example, a connection object 
   in a network library where you may have many options like timeout settings, retry policies, etc.
4. Readability and Maintainability: Enhances the readability and maintainability of the code by separating the 
   construction logic from the object itself.
"""

class House:
    def __init__(self, foundation, structure, roof, has_garage=False, has_swimming_pool=False):
        self.foundation = foundation
        self.structure = structure
        self.roof = roof
        self.has_garage = has_garage
        self.has_swimming_pool = has_swimming_pool

    def __str__(self):
        return f"House with {self.foundation} foundation, {self.structure} structure, {self.roof} roof" + \
               (f", a garage" if self.has_garage else "") + \
               (f", and a swimming pool" if self.has_swimming_pool else "")

class HouseBuilder:
    def __init__(self, foundation, structure, roof):
        self.foundation = foundation
        self.structure = structure
        self.roof = roof
        self.has_garage = False
        self.has_swimming_pool = False

    def add_garage(self, has_garage):
        self.has_garage = has_garage
        return self

    def add_swimming_pool(self, has_swimming_pool):
        self.has_swimming_pool = has_swimming_pool
        return self

    def build(self):
        return House(self.foundation, self.structure, self.roof, self.has_garage, self.has_swimming_pool)

# Usage
builder = HouseBuilder("concrete", "wood", "shingles")
house = builder.add_garage(True).add_swimming_pool(True).build()
print(house)

"""
# Builder Pattern in a Nutshell:
The Builder Pattern is like a construction plan for building something complex, step by step, with options to add various features. Imagine you are building a sandwich with many layers and optional ingredients.

# Scenario:
Let's say we want to build a house. A house can have basic parts like a foundation, structure, and roof, but it can also have optional parts like a garage and a swimming pool.

# Components:
House: This is the final product.
HouseBuilder: This is the helper that builds the house step by step.

# Building the House:
Start with the Basic Parts: We define the foundation, structure, and roof.
Add Optional Features: We can add features like a garage and a swimming pool.

# Explanation in Simple Terms:
House Class: This class represents a house. It has basic parts like foundation, structure, and roof. It also has optional features like a garage and a swimming pool.
HouseBuilder Class: This class helps build the house. It starts with the basic parts (foundation, structure, roof) and provides methods to add optional features (garage and swimming pool).
Usage: We create a HouseBuilder object, set its various properties (e.g., adding a garage and swimming pool), and finally create a House object using the build method.

# Step-by-Step Creation:
1. Create a HouseBuilder with the basic parts.
2. Add optional features using builder methods (e.g., add_garage and add_swimming_pool).
3. Build the final House object.

In this way, you can easily construct a complex object (House) with various optional features in a readable and manageable way.

I hope this simplified explanation helps! If you have any further questions or need more clarification, feel free to ask.


"""