
# prompt user for path
path = input("Enter fully qualified path name (in double quotes) of the file with data: ")

try:
    f = open(path, 'r')  # open file
    counter = 0
    for line in f:
        mylist = line.split(' ')  # split string into tokens
        num1 = int(mylist[0])  # convert string to integer
        num2 = int(mylist[1])  # convert string to integer
        counter = counter + 1
        print "Line number: ",counter," Integer 1 = ",num1," Integer 2 = ",num2  # print values
except:
    print "Input error. Program terminates"