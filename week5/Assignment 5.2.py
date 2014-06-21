"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the sample output below. 

"""

#output:
#Invalid input
#Maximum is 7
#Minimum is 4

largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == 'done':
            break;
        n = int(num)
        largest = num if largest<num or largest == None else largest
        smallest = num if smallest>num or smallest == None else smallest
    except:
        print "Invalid input"
    #print num

print "Maximum is", largest
print "Minimum is", smallest
