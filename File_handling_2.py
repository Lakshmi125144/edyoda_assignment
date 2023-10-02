class Dog: 
    def __init__(self, name, age, coat_color): 
        self.name = name 
        self.age = age 
        self.coat_color = coat_color 
    def description(self): 
        print(f"The dog's name is {self.name} and it is {self.age} years old.") 
    def get_info(self): 
        print(f"The dog's coat color is {self.coat_color}.") 
class JackRussellTerrier(Dog): 
    def __init__(self, name, age, coat_color, eye_color): 
        super().__init__(name, age, coat_color) 
        self.eye_color = eye_color 
    def bark(self): 
        print("Woof!") 
class Bulldog(Dog): 
    def __init__(self, name, age, coat_color, underbite): 
        super().__init__(name, age, coat_color) 
        self.underbite = underbite 
    def snore(self): 
        print("Zzz...") 
# Create objects 
jack_russell_terrier = JackRussellTerrier("Jack", 5, "White and brown", "Brown") 
bulldog = Bulldog("Bulldog", 7, "Brindle", True) 
# Implement the above functionalities 
jack_russell_terrier.description() 
jack_russell_terrier.get_info() 
jack_russell_terrier.bark() 
bulldog.description() 
bulldog.get_info() 
bulldog.snore()
