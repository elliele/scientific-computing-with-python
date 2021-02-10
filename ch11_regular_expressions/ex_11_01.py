'''
Write a simple program to simulate the operation of the the grep command on
Unix. Ask the user to enter a regular expression and count the number of
lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
'''


import re
grep = input('Enter a regular expression: ')
hand = open('mbox-short.txt')
count = 0
for line in hand:
    line = line.rstrip()
    if re.search('\\b' + grep + '\\b', line):
        count = count + 1
print('mbox-short.txt had',count, 'lines that matched', grep)
