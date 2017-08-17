# Function with Nested IF Else
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

printColor('r')  # call function
