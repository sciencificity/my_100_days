# run at terminal $ using python day60.py
import itertools
import sys
import time 
import random

from termcolor import colored

symbols = itertools.cycle('-\|/')

count = 0
while count < 50:
    count += 1
    sys.stdout.write('\r' + next(symbols))
    sys.stdout.flush() # make sure it goes to screen
    time.sleep(0.3) # sleep for 1 second
    
# Traffic lights my try
print(colored('hello', 'red'), colored('world', 'green'), '\n')
# colors = list(red.range_to(Color("green"),10))
colours = []
colours.append(colored('red     ', 'red'))
colours.append(colored('green   ', 'green'))
colours.append(colored('yellow  ', 'yellow'))

cols = itertools.cycle(colours)

count = 0
while count < 40:
    count += 1
    sys.stdout.write('\r' + next(cols))
    sys.stdout.flush() # make sure it goes to screen
    time.sleep(2) # sleep for 2 second
    

# colour_lst = 'Red Green Amber'.split()
# rotation = itertools.cycle(colour_lst)
# 
# def light_rotate(rotation):
#     for colour in rotation:
#         if colour == 'Amber':
#             print(f'Caution! The light is {colour}')
#             time.sleep(3)
#         elif colour == 'Red':
#             print(f'Stop! The light is {colour}')
#             time.sleep(2)
#         else:
#             print(f'Go! The light is {colour}')
#             time.sleep(3)
# 
# light_rotate(rotation)        


