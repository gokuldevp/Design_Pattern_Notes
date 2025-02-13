### **What are Structural Design Patterns?**

Structural design patterns are a category of design patterns that deal with **object composition** and **class relationships**. They help you organize classes and objects into larger structures while keeping these structures flexible and efficient. These patterns focus on how classes and objects are composed to form larger structures, ensuring that the system remains scalable and maintainable.

#### **Why are they important?**
1. **Flexibility**: They allow you to change the structure of objects without changing their behavior.
2. **Reusability**: They promote reusable code by defining clear relationships between classes and objects.
3. **Maintainability**: They make your code easier to maintain by decoupling the system's components.
4. **Scalability**: They help in building scalable systems by organizing classes and objects efficiently.

#### **When to use structural design patterns?**
- When you need to add new functionalities to existing classes without modifying their structure.
- When you want to simplify the relationships between classes and objects.
- When you need to create complex structures from simple components.
- When you want to ensure that the system remains flexible and adaptable to changes.

---

### **Types of Structural Design Patterns**

There are seven main structural design patterns:

1. **Adapter Pattern**: Allows incompatible interfaces to work together.
2. **Bridge Pattern**: Separates an object’s abstraction from its implementation.
3. **Composite Pattern**: Composes objects into tree structures to represent part-whole hierarchies.
4. **Decorator Pattern**: Adds additional responsibilities to an object dynamically.
5. **Facade Pattern**: Provides a simplified interface to a complex subsystem.
6. **Flyweight Pattern**: Reduces the cost of creating and manipulating a large number of similar objects.
7. **Proxy Pattern**: Provides a surrogate or placeholder for another object to control access to it.

---

### **1. Adapter Pattern**

**Concept**:  
Allows objects with **incompatible interfaces** to collaborate by converting the interface of one class into another interface that clients expect.

**Problem**:  
- How to make two incompatible interfaces work together without modifying their existing code?

**Solution**:  
- Create an **adapter class** that acts as a bridge between the two incompatible interfaces.

**Real-world analogy**:  
A power adapter that allows a device with a foreign plug to work with a local power outlet.

**Code Example**:  
```python
# Object Adapter (Using Composition)
class EnglishSpeaker:
    def speak_english(self):
        pass

class FrenchSpeaker:
    def speak_french(self):
        return "Bonjour!"

class TranslatorAdapter(EnglishSpeaker):
    def __init__(self, french_speaker):
        self.french_speaker = french_speaker

    def speak_english(self):
        return self.french_speaker.speak_french()

# Usage
french_speaker = FrenchSpeaker()
translator = TranslatorAdapter(french_speaker)
print(translator.speak_english())  # Output: Bonjour!


# Class Adapter (Using Inheritance)
class FrenchSpeaker:
    def speak_french(self):
        return "Bonjour!"

class EnglishSpeaker:
    def speak_english(self):
        pass

class TranslatorAdapter(EnglishSpeaker, FrenchSpeaker):
    def speak_english(self):
        return self.speak_french()

# Usage
translator = TranslatorAdapter()
print(translator.speak_english())  # Output: Bonjour!

```

**When to use**:  
- Integrating third-party libraries with different interfaces.
- Reusing existing classes with incompatible interfaces.

**Pros**:  
- Promotes reusability of existing code.
- Decouples the client from the adaptee.

**Cons**:  
- Can introduce additional complexity.

**Interview Tip**:  
- Mention the difference between **class adapter** (using inheritance) and **object adapter** (using composition).

---

### **2. Bridge Pattern**

**Concept**:  
Separates an object’s **abstraction** from its **implementation** so that the two can vary independently.

**Problem**:  
- How to avoid a permanent binding between an abstraction and its implementation?

**Solution**:  
- Use a **bridge** to separate the abstraction and implementation into different class hierarchies.

**Real-world analogy**:  
A remote control (abstraction) and a TV (implementation). The remote can work with different types of TVs.

**Code Example**:  
```python
# Implementation Interface
class Device:
    def is_enabled(self):
        pass

    def enable(self):
        pass

    def disable(self):
        pass

# Concrete Implementation
class TV(Device):
    def __init__(self):
        self._on = False

    def is_enabled(self):
        return self._on

    def enable(self):
        self._on = True
        print("TV is enabled")

    def disable(self):
        self._on = False
        print("TV is disabled")

# Abstraction
class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

# Usage
tv = TV()
remote = RemoteControl(tv)
remote.toggle_power()  # Output: TV is enabled
remote.toggle_power()  # Output: TV is disabled
```

**When to use**:  
- When you want to avoid a permanent binding between an abstraction and its implementation.
- When both the abstraction and implementation need to be extended independently.

**Pros**:  
- Promotes flexibility and extensibility.
- Decouples the abstraction from the implementation.

**Cons**:  
- Can increase the complexity of the code.

**Interview Tip**:  
- Explain how the Bridge Pattern differs from the Adapter Pattern (Bridge is designed upfront, Adapter is used to make existing classes work together).

---

### **3. Composite Pattern**

**Concept**:  
Composes objects into **tree structures** to represent part-whole hierarchies. It allows clients to treat individual objects and compositions uniformly.

**Problem**:  
- How to represent part-whole hierarchies of objects in a way that clients can treat individual objects and compositions uniformly?

**Solution**:  
- Use a **composite class** that can contain both individual objects and other composite objects.

**Real-world analogy**:  
A file system where directories can contain files and other directories.

**Code Example**:  
```python
# Component Interface
class FileSystemComponent:
    def display(self):
        pass

# Leaf
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"File: {self.name}")

# Composite
class Directory(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def display(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.display()

# Usage
root = Directory("Root")
file1 = File("File1")
file2 = File("File2")
sub_dir = Directory("Sub Directory")
sub_dir.add(file1)
root.add(file2)
root.add(sub_dir)
root.display()
```

**When to use**:  
- Representing hierarchical structures like file systems, organization charts, etc.
- When you want clients to treat individual objects and compositions uniformly.

**Pros**:  
- Simplifies client code by treating individual objects and compositions uniformly.
- Makes it easy to add new types of components.

**Cons**:  
- Can make the design overly general (hard to restrict components).

**Interview Tip**:  
- Mention the **transparency** vs. **safety** trade-off (whether to include child management methods in the component interface).

---

### **4. Decorator Pattern**

**Concept**:  
Adds **additional responsibilities** to an object dynamically without altering its structure. It provides a flexible alternative to subclassing for extending functionality.

**Problem**:  
- How to add responsibilities to objects dynamically and transparently without affecting other objects?

**Solution**:  
- Use a **decorator class** that wraps the original object and adds new behaviors.

**Real-world analogy**:  
Adding toppings to a pizza (the base pizza remains the same, but you can add extra cheese, pepperoni, etc.).

**Code Example**:  
```python
# Component Interface
class Coffee:
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Decorator
class MilkDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1

# Usage
coffee = SimpleCoffee()
print(coffee.cost())  # Output: 5

milk_coffee = MilkDecorator(coffee)
print(milk_coffee.cost())  # Output: 7

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(sugar_milk_coffee.cost())  # Output: 8
```

**When to use**:  
- Adding responsibilities to objects dynamically and transparently.
- When subclassing is impractical due to a large number of possible extensions.

**Pros**:  
- Provides a flexible alternative to subclassing.
- Follows the **Open/Closed Principle** (open for extension, closed for modification).

**Cons**:  
- Can result in many small classes, making the system harder to understand.

**Interview Tip**:  
- Explain how the Decorator Pattern differs from inheritance (decorators add behavior at runtime, inheritance adds behavior at compile time).

---

### **5. Facade Pattern**

**Concept**:  
Provides a **simplified interface** to a complex subsystem, making it easier to use.

**Problem**:  
- How to simplify the interaction with a complex system or library?

**Solution**:  
- Create a **facade class** that provides a simple interface to the complex system.

**Real-world analogy**:  
A customer service representative who handles all the complexities of interacting with different departments in a company.

**Code Example**:  
```python
# Subsystem Classes
class CPU:
    def start(self):
        print("CPU is starting")

class Memory:
    def load(self):
        print("Memory is loading")

class HardDrive:
    def read(self):
        print("Hard Drive is reading")

# Facade
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.start()
        self.memory.load()
        self.hard_drive.read()

# Usage
computer = ComputerFacade()
computer.start()
```

**When to use**:  
- Simplifying interaction with a complex system or library.
- Providing a higher-level interface to a subsystem.

**Pros**:  
- Simplifies the usage of complex systems.
- Decouples the client from the subsystem.

**Cons**:  
- Can become a "god object" if not used carefully.

**Interview Tip**:  
- Mention how the Facade Pattern can be used to wrap legacy systems.

---

### **6. Flyweight Pattern**

**Concept**:  
Reduces the cost of creating and manipulating a large number of similar objects by sharing as much data as possible.

**Problem**:  
- How to manage a large number of similar objects efficiently?

**Solution**:  
- Use a **flyweight factory** to share common state between objects.

**Real-world analogy**:  
A text editor that shares character objects to save memory (e.g., storing only one instance of each character).

**Code Example**:  
```python
# Flyweight
class Character:
    def __init__(self, char):
        self.char = char

    def display(self, font_size):
        print(f"Character: {self.char}, Font Size: {font_size}")

# Flyweight Factory
class CharacterFactory:
    _characters = {}

    @classmethod
    def get_character(cls, char):
        if char not in cls._characters:
            cls._characters[char] = Character(char)
        return cls._characters[char]

# Usage
factory = CharacterFactory()
char_a = factory.get_character('A')
char_a.display(12)  # Output: Character: A, Font Size: 12

char_b = factory.get_character('B')
char_b.display(14)  # Output: Character: B, Font Size: 14

char_a_again = factory.get_character('A')
char_a_again.display(16)  # Output: Character: A, Font Size: 16
```

**When to use**:  
- When a large number of similar objects need to be managed efficiently.
- When memory usage is a concern.

**Pros**:  
- Reduces memory usage by sharing common state.
- Improves performance by reducing object creation overhead.

**Cons**:  
- Can introduce complexity in managing shared state.

**Interview Tip**:  
- Explain the difference between **intrinsic** (shared) and **extrinsic** (unique) state in the Flyweight Pattern.

---

### **7. Proxy Pattern**

**Concept**:  
Provides a **surrogate or placeholder** for another object to control access to it.

**Problem**:  
- How to control access to an object (e.g., lazy initialization, access control, logging)?

**Solution**:  
- Use a **proxy class** that acts as an intermediary between the client and the real object.

**Real-world analogy**:  
A credit card is a proxy for a bank account—it controls access to the account.

**Code Example**:  
```python
# Subject Interface
class Image:
    def display(self):
        pass

# Real Subject
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")

# Proxy
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# Usage
image = ProxyImage("test_image.jpg")
image.display()  # Output: Loading image: test_image.jpg, Displaying image: test_image.jpg
image.display()  # Output: Displaying image: test_image.jpg
```

**When to use**:  
- Lazy initialization of expensive objects.
- Access control (e.g., protecting sensitive objects).
- Logging or monitoring object access.

**Pros**:  
- Provides controlled access to the real object.
- Can add additional functionality (e.g., logging, caching).

**Cons**:  
- Can introduce additional complexity.

**Interview Tip**:  
- Mention different types of proxies (e.g., virtual, protection, remote).

---

### Final Interview Tips:  
1. **Use analogies**: Relate patterns to real-world scenarios (e.g., Adapter as a power adapter, Proxy as a credit card).  
2. **Focus on intent**: Start with the problem the pattern solves.  
3. **Compare patterns**: Know when to use Adapter vs. Bridge, Decorator vs. Proxy, etc.  
4. **Code structure**: Highlight how patterns decouple code and promote flexibility.  
5. **Real-world examples**: Be ready to provide examples from your experience or common systems (e.g., file systems, UI libraries).