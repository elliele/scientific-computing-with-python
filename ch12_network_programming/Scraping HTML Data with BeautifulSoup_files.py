# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 20:39:28 2021

@author: Ellie Le
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
count = 0

tags = soup('span')
for tag in tags:
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
    num = int(tag.contents[0])
    sum = sum + num
    count = count + 1
    
print('Count', count)
print ('Sum', sum)