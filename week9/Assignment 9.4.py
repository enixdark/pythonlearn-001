"""
9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the senders mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

#output
#cwen@iupui.edu 5

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
f = open(name)

dic = {}
maxvalue = 0
name = ""
l = [i.split()[1] for i in f.readlines() 
            if i.startswith("From") and i.find("@")>0 and len(i.split()) > 2]
for i in l:
    if not dic.has_key(i):
        dic[i] = 1
    else:
        dic[i] +=1
        if maxvalue < dic[i]:
            maxvalue = dic[i]
            name = i

print name,maxvalue
