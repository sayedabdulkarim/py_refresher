# a = [1,2,2,3,3]
# print(set(a))
# print(a)

class Dog():

    species = "MAMMAL"
    
    def __init__(self, breed, name, spots):
        # attributes
        self.breed = breed
        self.name = name
        self.spots = spots
        
        #Actions/ methods 
    def bark(self, number):
        print("WOOOOOOF, My name is {}, and my number is {}".format(self.name, number))

# 
myDog = Dog(breed= "Poekmon", name="Tuffy", spots=2)
# print(myDog.spots)
# print(myDog.species)
myDog.bark(12)