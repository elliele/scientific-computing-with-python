# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:30:08 2021

@author: Ellie Le

"""

"""
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to
 http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
 read the JSON data from that URL using urllib and then parse and extract
 the comment counts from the JSON data, compute the sum of the numbers in
 the file and enter the sum below:
     
We provide two files for this assignment. One is a sample file where we give
 you the sum for your testing and the other is the actual data you need to
 process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1143571.json 
(Sum ends with 28)
You do not need to save these files to your folder since your program will
 read the data directly from the URL. Note: Each student will have a distinct 
 data url for the assignment - so only use your own data url for analysis.
"""
import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

total = 0
count = 0

info = json.loads(data)

for item in info['comments']:
    #print (item['count'])
    total = total + item['count']
    count = count + 1

print('Count:', count )
print('Sum:', total)

