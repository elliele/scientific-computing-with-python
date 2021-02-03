"""
Exercise 4: Add code to the above program to figure out who has the most 
messages in the file. After all the data has been read and the dictionary has 
been created, look through the dictionary using a maximum loop (see Chapter 5: 
Maximum and minimum loops) to find who has the most messages and print how 
many messages the person has.

Output
-----

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
fname = input('Enter a file name: ')
fhand = open(fname)

email = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        if words [1] not in email:
            email[words[1]] = 1
        else:
            email[words[1]] += 1
#print(email)

largest = -1
theword = None
for k,v in email.items():
    #print(k,v)
    if v > largest :
        largest = v
        theword = k # capture/remember the key that was largest
print(theword, largest)
