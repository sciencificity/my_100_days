
print(set(['foo', 'bar']))

print(set({'hello': 5}))

print(set('hello')) # throws away duplicate letters, and is unordered
print(list('hello')) # keeps all duplicates, and the order

x = {'foo', 'bar'}
print(x)

# To define an empty set you can't use {} since that is a dict
# use set() instead
y_dict = {}
print(type(y_dict))

y_set = set()
print(type(y_set))

# Length set - use len
a = {1,1,2}
print(f'a is {a} and length of a is {len(a)}')

b = {(1,2), 3}
print(f'b is {b} and length of b is {len(b)}')

# To check if elem in the set use `in`

# Cannot slice or index sets as they are unordered

# To loop however you can do like normal

import timeit
def init_set():
    s = set()
    for i in range(1000):
        s.add(i)
    return s

# print(timeit.repeat(stmt=init_set,
#                     number=10000,
#                     repeat=3))
                    
                    
def init_lst():
    lst = list()
    for i in range(1000):
        lst.append(i)
    return lst
# 
# print(timeit.repeat(stmt=init_lst,
#                     number=10000,
#                     repeat=3))
#                     
                    
def init_tup():
    tup = tuple()
    for i in range(1000):
        tup += (i, ) # tuples are immutable so we cannot , which is also why it takes longer
    return tup

# print(timeit.repeat(stmt=init_tup,
#                     number=10000,
#                     repeat=3))             
                    
                    
s = init_set()
lst = init_lst()
tup = init_tup()

def member_set():
    for i in range(1000):
        i in s
        

print(timeit.repeat(stmt=member_set,
                    number=10000,
                    repeat=2))
        
def member_lst():
    for i in range(1000):
        i in lst    
        
print(timeit.repeat(stmt=member_lst,
                    number=1000,
                    repeat=2))        
        
def member_tup():
    for i in range(1000):
        i in tup   
        
print(timeit.repeat(stmt=member_tup,
                    number=1000,
                    repeat=2))        
