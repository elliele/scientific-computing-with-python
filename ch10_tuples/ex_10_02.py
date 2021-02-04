"""
Exercise 2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string 
into parts using the colon character. Once you have accumulated the counts for each hour, print 
out the counts, one per line, sorted by hour as shown below.

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)

time = dict()
for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From':
        continue

    col_pos = words[5].find(':')
    hour = words[5][:col_pos]
    if hour not in time:
        time[hour] = 1      # First entry
    else:
        time[hour] += 1

lst = sorted([ (k,v) for k,v in time.items() ])
#print(lst)

for k,v in lst:
    print(k,v)
