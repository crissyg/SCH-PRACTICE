choice = 0;   # to make while loop condition True on first execution
while (choice != 3):   # loop as long as no value 3 for choice

    try:
        # menu display
        print("\n   MENU")
        print("1. print hello")
        print("2. print hi")
        print("3. exit")
        choice = input("Please enter your choice (1, 2, or 3): ")

        # menu processing
        if (choice == 1):
            print "\nhello"
        elif (choice == 2):
            print "\nhi"
        elif (choice == 3):
            print "" # do nothing
        else:   # invalid choice
            print("\nThis is not a valid integer choice. Please enter again")  # for all integers not 1-3
    except:
        print("\nThis is not a valid choice. Please enter valid integer for the choice") # for all non-integers