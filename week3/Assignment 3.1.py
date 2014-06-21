
"""3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award time-and-a-half for the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly. 
"""

#output:
#498.75

try:
	h = raw_input("please input your hour:")
	hour = float(h)
	r = raw_input("please input your rate:")
	rate = float(r)
	if hour < 0:
		print "Please,input your positive numberic"
	elif rate < 0:
		print "Please,input your positive numberic"
	elif hour > 40:
		print "%.2f" % (40*rate+(hour-40)*1.5*rate)
	else:
		print "%.2f" % (hour*rate)
except:
		print "Please,input your numberic"



