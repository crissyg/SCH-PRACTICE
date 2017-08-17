# prompt user for path
path = input("Enter fully qualified path name (in double quotes) of the file with data: ")

firstValues = [100]
secondValues = [100]

try:
    f = open(path, 'r')  # open file
    counter = 0
    for line in f:
        mylist = line.split(' ')  # split string into integer tokens
        firstValues.append(int(mylist[0]))
        secondValues.append(int(mylist[1]))
        counter = counter + 1

    num = 0
    while (num < counter):
        print "Line number: ",counter," Integer 1 = ",firstValues[num]," Integer 2 = ",secondValues[num]  # print values
        num = num + 1
except:
    print "Input error. Program terminates"