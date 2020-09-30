"""
 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and coput the average of those values and produce an output as shown below.

You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

#output:
#Average spam confidence: 0.750718518519

# Updated assignment asks users to not use sum() function or variable name in their solution
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if len(fname) == 0:
    fname = 'mbox-short.txt'
fh = open(fname)
c = 0
t = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    c = c + 1
    n = float(line[21:])
    t = n + t
ans = t / c
print("Average spam confidence:", ans)
