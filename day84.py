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
# array([  1.     ,   4.09375,   7.1875 ,  10.28125,  13.375  ,  16.46875,
#         19.5625 ,  22.65625,  25.75   ,  28.84375,  31.9375 ,  35.03125,
#         38.125  ,  41.21875,  44.3125 ,  47.40625,  50.5    ,  53.59375,
#         56.6875 ,  59.78125,  62.875  ,  65.96875,  69.0625 ,  72.15625,
#         75.25   ,  78.34375,  81.4375 ,  84.53125,  87.625  ,  90.71875,
#         93.8125 ,  96.90625, 100.     ])

# linspace by default includes the stop number which
# is diff to arange BUT what if I did not want the 100
# in my array?? -> use endpoint = False
np.linspace(1, 100, num=33, endpoint=False)
# array([ 1.,  4.,  7., 10., 13., 16., 19., 22., 25., 28., 31., 34., 37.,
#        40., 43., 46., 49., 52., 55., 58., 61., 64., 67., 70., 73., 76.,
#        79., 82., 85., 88., 91., 94., 97.])

# similar is the np.logspace which just takes
# the log of the linspace
np.logspace(1, 100, num=33, endpoint = False)
# array([1.e+01, 1.e+04, 1.e+07, 1.e+10, 1.e+13, 1.e+16, 1.e+19, 1.e+22,
#        1.e+25, 1.e+28, 1.e+31, 1.e+34, 1.e+37, 1.e+40, 1.e+43, 1.e+46,
#        1.e+49, 1.e+52, 1.e+55, 1.e+58, 1.e+61, 1.e+64, 1.e+67, 1.e+70,
#        1.e+73, 1.e+76, 1.e+79, 1.e+82, 1.e+85, 1.e+88, 1.e+91, 1.e+94,
#        1.e+97])

# another is the geometric function
np.geomspace(1, 100, num=33, endpoint = False)
# array([ 1.        ,  1.149757  ,  1.32194115,  1.51991108,  1.7475284 ,
#         2.009233  ,  2.3101297 ,  2.65608778,  3.05385551,  3.51119173,
#         4.03701726,  4.64158883,  5.33669923,  6.13590727,  7.05480231,
#         8.11130831,  9.32603347, 10.72267222, 12.32846739, 14.17474163,
#        16.29750835, 18.73817423, 21.5443469 , 24.77076356, 28.48035868,
#        32.74549163, 37.64935807, 43.28761281, 49.77023564, 57.22367659,
#        65.79332247, 75.64633276, 86.97490026])

# Grid
x = np.array([1,2,3,4])
y = np.array([5,6,7,8])
np.meshgrid(x,y)
