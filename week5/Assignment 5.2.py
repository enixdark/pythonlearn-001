"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the sample output below. 

"""

#output:
#Invalid input
#Maximum is 7
#Minimum is 4

l = None
s = None
while True:
    try:
        n = input("Enter a number: ")
        if n == 'done':
            break;
        n1 = int(num)
        l = n if l<n or l == None else l
        s= n if s>n or s == None else s
    except:
        print("Invalid input")
    #print n

print "Maximum is", l
print "Minimum is", s
