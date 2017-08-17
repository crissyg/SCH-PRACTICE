class Person:

    def __init__(self, ageParm, idParm):
        self.age = ageParm
        self.id = idParm

    def setAge(self, ageParm):
        self.age += ageParm

    def setID(self, idParm):
        self.id += idParm

    def getAge(self):
        return self.age

    def getID(self):
        return self.id

# create list
#myList = []

# add a few instances of Person
#myList.append(Person(20,101))
#myList.append(Person(30,102))
#myList.append(Person(40,103))

#print "ages="
#for person in myList:
#    print person.getAge()









