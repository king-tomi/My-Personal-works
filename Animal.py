class Animal:
    
    def speak(self):
        print("Hello World!")
        
    def reply(self):
        self.speak()
        
class Mammal(Animal):
    
    def speak(self):
        super().speak()
        
class Dog(Mammal):
    
    def speak(self):
        print("Woof!")
        
class Cat(Mammal):
    
    def speak(self):
        print("meow!!!")
        
class Primate(Mammal):
    
    def speak(self):
        super().speak()
        
class Hacker(Primate):
    pass
    
    
if __name__ == "__main__":
    kitty = Cat()
    bob = Hacker()
    kitty.reply()
    bob.reply()