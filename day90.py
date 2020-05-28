"18/03/2020"

my_range = range(1, 21)
print([str(x) for x in my_range]) # convert to string
print(list(map(str, my_range))) # alt of above

##############################
a = ["1", 1, "1", 2]
print(list(set(a)))
# Alt 1
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)
# Explanation of Alt1
# Ordered dictionaries are another data type in Python that unlike sets 
# and normal dictionaries they preserve the order of the items. 
# Here OrderedDict.fromkeys(a)  would produce an OrderedDict  
# like [('1', None), (1, None), (2, None)] . Then we would convert that 
# OrderedDict  to a list.

# Alt 2
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
# Explanation Alt 2: 
# This is another solution that would preserve the original order. 
# We go through all items of the original list and append them to the 
# new list if they have not been appended before. The downside of 
# this is the operation can take a lot of time if the list is large 
# as we need to access both lists and also perform a conditional in 
# each iteration. 

##############################

# Calculate the sum of all dictionary values.
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))
# d.values()  returns a list-like dict_values  object while the sum  
# function calculates the sum of the dict_values  items.

# Question: Filter the dictionary by removing all items with a value of 
# greater than 1.
print({val for val in d.items() if val[1] <= 1})
# Alt
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)
print(dict({(key, value) for key, value in d.items() if value <= 1}))

# Create a dictionary of keys a, b, c where each key has as value 
# a list from 1 to 10, 11 to 20, and 21 to 30 respectively. 
# Then print out the dictionary in a nice format.
from pprint import pprint
d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)
print(d['b'][2])

# Create a function that takes any string as input and returns the 
# number of words for that string.
def count_words(strng): 
    strng_list = strng.split() 
    return len(strng_list) 
 
print(count_words("Hey there it's me!"))
# We're using split  here which is a string method that splits a string 
# into several strings given a separator passed inside the brackets. 
# When you don't pass a separator, split  will split a string at white spaces. 
# This will output a list of strings..Applying len  to that list 
# returns the number of list items, so the number of words.

def count_words(filepath):
    with open(filepath, 'r') as file:
        strng = file.read()
        strng_list = strng.split(" ")
        return len(strng_list)
 
print(count_words("original.txt"))

def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)
 
print(count_words("original2.txt"))

import re
 
def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(",| ", text)
    return len(string_list)
 
print(count_words_re("original2.txt"))

# This alternative solution uses the built-in re  module which provides 
# regular expression matching operations. We're using the split method of 
# that module and the expression ",| " is meant to replace commas with spaces. 
# Using methods from the re  module can be more appropriate than Python 
# built-in methods when string operations are complicated. However, for 
# this simple scenario the re  module could be skipped.
