def printColor(value):
    value = value.upper()
    if (value == 'Y'):
        print "yellow"
    elif (value == 'B'):
        print "blue"
    elif (value == 'R'):
        print "red"
    else:
        print "unknown"

# code to test
printColor('r')  # call function