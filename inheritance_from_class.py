class animal(object):
    def __init__(self,name,age,color,voice,type):
        self.name=name
        self.age=age
        self.color=color
        self.voice=voice
        self.type=type
    
    def animal_type(self):
        print("Hi I am", self.name,"I am", self.age,"years old", "I am a", self.type)
        
    def animal_speak(self):
        print("Hi I am", self.name, "I go ", self.voice)
        

class Dog(animal):         # Class Dog inherit properties from animal class so you don't have to re-write, just add additional attributes, I added "breed"
    def __init__(self,name,age,color,voice,type,breed):
        super().__init__(name,age,color,voice,type)
        self.breed=breed
        
class Cat(animal):     #Class Cat inherit properties from animal class so you don't have to re-write, just add additional attributes, here I added "pet"
    def __init__(self,name,age,color,voice,type,pet):
        super().__init__(name,age,color,voice,type)
        self.pet=pet
    


pup=Dog('pup','5','brown','Bark bark','dog','nice')
kitty= Cat('kitty', '3','white','meow','cat','pet')

pup.animal_speak()    # output: Hi I am pup I go  Bark bark
kitty.animal_speak()   # Hi I am kitty I go  meow
kitty.animal_type()   # Hi I am kitty I am 3 years old I am a cat
pup.animal_type()   #Hi I am pup I am 5 years old I am a dog
