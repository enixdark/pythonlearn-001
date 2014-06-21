"""
3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 
"""
# output:
#B

try:
    s = raw_input("please input your score:")
    score = float(s)
    if score > 1.0:
        print "value out of range"
    elif 1.0 >= score>=.9:
        print "A"
    elif .9 > score>=.8:
        print "B"
    elif .8 >score>=.7:
        print "D"    
    elif .7 >score>=.6:
        print "D"
except:
    print "Error , please input is numeric"
   
