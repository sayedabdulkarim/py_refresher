# a = [1,2,2,3,3]
# print(set(a))
# print(a)

class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

# 
myDog = Dog(breed= "Poekmon", name="Tuffy", spots=2)
print(myDog.spots)
# print(type(myDog))