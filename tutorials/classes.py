class Dog:
    def __init__(self, name):
        self.name = name # public
        # self._name = name # protected
        # self.__name = name # private        
        self.age = 0

    def setName(self, name):
            self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

dogs = []

# different ways of creating a Dog instance

dog1 = Dog("Roofus")
dog1.age = 7
dogs.append(dog1)

dog2 = Dog("")
dog2.name = "Bob"
dog2.age = 3
dogs.append(dog2)

dog3 = Dog("Fluffy")
dog3.setAge(1)
dogs.append(dog3)

dog4 = Dog("Tony")
dog4.age = dog1.getAge()
dogs.append(dog4)

# user input
# dog1.name = input()
# dog1.age = int(input())

# print an array of classes
print("I have " + str(len(dogs)) + " dogs.")
for i in range(0,len(dogs)):  
    print(dogs[i].name + " is " + str(dogs[i].age) + " year(s) old.")
