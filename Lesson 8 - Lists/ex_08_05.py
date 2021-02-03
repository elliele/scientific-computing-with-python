'''
Exercise 5: Write a program to read through the mail box data and when you 
find line that starts with “From”, you will split the line into words using 
the split function. We are interested in who sent the message, which is the 
second word on the From line.


Output
----

From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

"""

fname = input("Enter file name: ")

fh = open(fname)
count = 0
for line in fh :
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print (words[1])
    count +=1
print("There were", count, "lines in the file with From as the first word")
