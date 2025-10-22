class animal (object):
    def __init__(self,name,color,race,age):
        self.name=name
        self.color=color
        self.race=race
        self.age=age
        
    def animal_color(self,color):
         self.color=color
         print("My name is", self.name, "my color is " ,self.color)
    
    def animal_race(self,race):
         self.race=race
    
    def animal_age(self,age):
        self.age=age
    
    def change_name(self,name):
        self.name=name
        print("my name is changed to", self.name)
        

pup=animal('Tommy','white','bulldog','3')   # class animal with defualt values of name, color, race and age
print(pup.race)  # this will simple print pup'race you provided in default i.e bulldog. 
print(pup.color)  # color will be White as default
pup.animal_color('grey')  # when a function is called, you can change default values now.. I changed color to grey
print(pup.race)
print(pup.color)         # now since we are printing color after the func "animal_color", the value will be grey
print(pup.name)          # default name is Tommy right now
print(pup.age)
pup.change_name('puppy')  # the name is now chamged to puppy
print(pup.name)           #the name is puppy now