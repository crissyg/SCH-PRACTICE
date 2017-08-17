#file name Person2 contains class called Person
from Person2 import Person

# create list
personList = []

# prompt user for path
path = input("Enter fully qualified path name (in double quotes) of the file with data: ")

try:
    f = open(path, 'r')  # open file
    counter = 0
    arraySize = 0
    for line in f:
        mylist = line.split(' ')  # split string into tokens
        counter = counter + 1
        ageValue = int(mylist[0])  # convert string to integer
        idValue = int(mylist[1])   # convert string to integer

        if (ageValue >= 0 and idValue >= 0):
            personList.append(Person(ageValue,idValue))
            arraySize = arraySize + 1

    print "Added ", arraySize, " sets of data"

except:
    print "Input error. Program terminates"


