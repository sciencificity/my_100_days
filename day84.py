# Day 84: np.arange 12th March
import numpy as np

np.arange(start=1, stop=10, step=1)
np.arange(1.0, 10.01, .2)
# desc array
np.arange(10, 0, -1)

x = np.arange(1, 10, dtype = np.int8) # signed
x.shape
x.reshape(3,3)
np.arange(0, 256, dtype = np.uint8) # unsigned int - nice for pics

# range is a class and only allows integers
# np.arange -> returns an array
# range -> numbers generated on demand
# numpy has lots of in built efficiency though

np.arange(1, 100, 1, dtype = np.int32)

# alt routine is linspace - here we can specify the 
# numbers we want e.g. 33
# gives us 33 evenly spaced numbers between 1 and 100
# linspace by default includes the stop number which
# is diff to arange!
np.linspace(1, 100, num=33)

# linspace by default includes the stop number which
# is diff to arange BUT what if I did not want the 100
# in my array?? -> use endpoint = False
np.linspace(1, 100, num=33, endpoint=False)

# similar is the np.logspace which just takes
# the log of the linspace
np.logspace(1, 100, num=33, endpoint = False)

# another is the geometric function
np.geomspace(1, 100, num=33, endpoint = False)

# Grid
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
np.meshgrid(x,y)
