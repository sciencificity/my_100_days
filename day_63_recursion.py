### Recursion
# Calls itself on a smaller version of itself.

def factorial_rec(n):
  '''
  n! = n * (n-1) * (n-2) * (n-3) * .... * 1
  n! = n * (n-1)!
  5! = 5 * 4! OR 5 * 4 * 3 * 2 * 1
  0! = 1
  '''
  if n <= 1:
    return 1
  else:
    return n * factorial_rec(n-1)
    
print(factorial_rec(5))

# factorial_rec(5)
# return 5 * factorial_rec(4)
#            return 4 * factorial_rec(3)
#                       return 3 * factorial_rec(2)
#                                  return 2 * factorial_rec(1)
#                                             return 1 


def deliver_presents_iteratively(houses):
  for house in houses:
    print('Delivering presents to', house)
    
    
def deliver_presents_recursively(houses):
    if len(houses) == 1:
        print("Delivering presents to", houses[0])
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # first elf
        deliver_presents_recursively(first_half)
        # second elf
        deliver_presents_recursively(second_half)
        
houses = [
  'Erics house',
  'Kennys house',
  'Kyles house',
  'Stans house'
]

deliver_presents_iteratively(houses)
deliver_presents_recursively(houses)


# Maintaining State - Thread the state
def sum_recursive(current_num, accum_sum):
  if current_num == 11:
    return accum_sum
  else:
    return sum_recursive(current_num + 1, accum_sum + current_num)

print(sum_recursive(1,0))

# Maintaining state - Global variables (NOT Recommended)
curr_num = 1
acc_sum = 0

def sum_rec2():
  global curr_num
  global acc_sum
  
  # base
  if curr_num == 11:
    return acc_sum
  else:
    acc_sum += curr_num
    curr_num += 1
    return sum_rec2()
    
print(sum_rec2())

from functools import lru_cache # caching option so we don't redo mult calls - cache decorator
from datetime import datetime 

def fibonacci_recursive(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
      return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_recursive_optimized(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_recursive_optimized(n - 1) + fibonacci_recursive_optimized(n - 2)
    
start_time = datetime.now()     
print(fibonacci_recursive(50))
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

start_time = datetime.now() 
print(fibonacci_recursive_optimized(50))
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))

import sys
print(sys.getrecursionlimit())

lst = list(range(750))
# It is recommended to use indexing rather than using slicing and creating copies of lists
# Naive way - NOT Optimal
start_time = datetime.now() 
def sum_lst(lst):
  if lst == []:
    return 0
  else:
    return lst[0] + \
          sum_lst(lst[1:])
print(sum_lst(lst))
          
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
          
start_time = datetime.now()          
def sum_lst_better(lst):
  def helper(start_ind):
    if start_ind == len(lst):
      return 0
    else:
      return lst[start_ind] + \
          helper(start_ind + 1)
  return helper(0)

print(sum_lst_better(lst))
time_elapsed = datetime.now() - start_time 
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
