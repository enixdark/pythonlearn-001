"""

8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

"""

#output:
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#zqian@umich.edu
#rjlowe@iupui.edu
#zqian@umich.edu
#rjlowe@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#gsilver@umich.edu
#gsilver@umich.edu
#zqian@umich.edu
#gsilver@umich.edu
#wagnermr@iupui.edu
#zqian@umich.edu
#antranig@caret.cam.ac.uk
#gopal.ramasammycook@gmail.com
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#david.horwitz@uct.ac.za
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#louis@media.berkeley.edu
#ray@media.berkeley.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#There were 27 lines in the file with From as the first word

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
c = 0
l = [i.split() for i in fh.readlines() 
            if i.startswith("From") and i.find("@")>0 and len(i.split())>2]
for i in l:
    print i[1]
    c+=1
print("There were", c, "lines in the file with From as the first word")
