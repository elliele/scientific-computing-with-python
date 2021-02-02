"""
Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:

X-DSPAM-Confidence: 0.8475
"""

fname = input('Enter the file name: ')
fhand = open(fname)

total = 0
count = 0
for line in fhand:
    if not line.startswith('X-DSPAM-Confidence:'): continue
    num = line.find("0")
    value = float(line[num:])
    count = count +1
    total = total + value

print('Average spam confidence:', total/count)
