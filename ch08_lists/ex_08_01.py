"""
Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. 
Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

"""
def chop(lst):
    del lst[0]
    del lst [-1]
    print(lst)

old = [1,2,3,4]
print(chop(old))

def middle(lst):
    new = lst[1:-1]
    return new

new = [1,2,3,4]
print(middle(new))
