x = int(input("Enter a number: ")) # to take input from the user and convert it to an integer
match x: # to use the match case statement to check the value of x
    case 0: # to check if x is 0
        print("Zero") # to print "Zero" if x is 0
    case 1: # to check if x is 1
        print("One") # to print "One" if x is 1
    case _ if 0 < x != 100: # to check if x is not 100
        print("Not Hundred") # to print "Not Hundred" if x is not 100
    case _ if x < 0: # to check if x is less than 0
        print("Negative") # to print "Negative" if x is less than 0
    case _: # to check if x does not match any of the above cases
        print("Other") # to print "Other" if x does not match any of the above cases
        