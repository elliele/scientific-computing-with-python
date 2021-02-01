"""
Exercise 5: Take the following Python code that stores a string:

str = 'X-DSPAM-Confidence:0.8475'

"""

text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find(':')
#print(atpos)

num = text[atpos +1 :]
#print(num)

value = float(num)
print(value)
