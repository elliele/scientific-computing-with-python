import re
hand = open('regex_sum_1143566.txt')
numlist = list()
num = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    for i in stuff:
        if i:
            i = int(i)
        numlist.append(i)

print(sum(numlist))
    #print(stuff)
