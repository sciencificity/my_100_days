import numpy as np 
s = np.array(5) # scalar
print(s.shape)
x = s + 3
print(x.shape)

v = np.array([1,2,3]) # vector
print(v.shape)
v[1:]

m = np.array([[1,2,3], [4,5,6], [7,8,9]]) # matrix
print(m.shape)
m[1][2]

t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]],[[[7],[8]],\
    [[9],[10]],[[11],[12]]],[[[13],[14]],[[15],[16]],[[17],[17]]]]) # tensor
print(t.shape)   
t[2][1][1][0]

v = np.array([1,2,3,4])
print(v)
x = v.reshape(1,4)
print(x)
x = v[None, :]
x

values = [1,2,3,4,5]
values = np.array(values) + 5 # first way
values
values += 5 # second way
values

a = np.array([[1,3],[5,7]])
a

b = np.array([[2,4],[6,8]])
b

a + b

a = np.array([[1,3],[5,7]])
a

c = np.array([[2,3,6],[4,5,9],[1,8,7]])
c

a.shape
c.shape
# a + c
# displays the following error:
# ValueError: operands could not be broadcast together with shapes (2,2) (3,3)

m = np.array([[1,2,3],[4,5,6]])
m
# displays the following result:
# array([[1, 2, 3],
#        [4, 5, 6]])

n = m * 0.25
n
# displays the following result:
# array([[ 0.25,  0.5 ,  0.75],
#        [ 1.  ,  1.25,  1.5 ]])

m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])

np.multiply(m, n)   # equivalent to m * n
# displays the following result:
# array([[ 0.25,  1.  ,  2.25],
#        [ 4.  ,  6.25,  9.  ]])


a = np.array([[1,2,3,4],[5,6,7,8]])
a
# displays the following result:
# array([[1, 2, 3, 4],
#        [5, 6, 7, 8]])
a.shape
# displays the following result:
# (2, 4)

b = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
b
# displays the following result:
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
b.shape
# displays the following result:
# (4, 3)

# Matrix Product
# To find the matrix product, you use NumPy's matmul function.
# If you have compatible shapes, then it's as simple as this:
c = np.matmul(a, b)
c
# displays the following result:
# array([[ 70,  80,  90],
#        [158, 184, 210]])
c.shape
# displays the following result:
# (2, 3)

# np.matmul(b, a)
# displays the following error:
# ValueError: shapes (4,3) and (2,4) not aligned: 3 (dim 1) != 2 (dim 0)
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, 
# with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 2 is different from 3)


# NumPy's dot function
# You may sometimes see NumPy's dot function in places where you would expect 
# a matmul. It turns out that the results of dot and matmul are the same if the 
# matrices are two dimensional.
# So these two results are equivalent:
a = np.array([[1,2],[3,4]])
a
# displays the following result:
# array([[1, 2],
#        [3, 4]])

np.dot(a,a)
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

a.dot(a)  # you can call `dot` directly on the `ndarray`
# displays the following result:
# array([[ 7, 10],
#        [15, 22]])

np.matmul(a,a)
# array([[ 7, 10],
#        [15, 22]])

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html#numpy.matmul
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html

# Transpose
# Getting the transpose of a matrix is really easy in NumPy. 
# Simply access its T attribute. There is also a transpose() function which 
# returns the same thing, but you'll rarely see that used anywhere because typing 
# T is so much easier. :)
# 
# For example:
m = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
m
# displays the following result:
# array([[ 1,  2,  3,  4],
#        [ 5,  6,  7,  8],
#        [ 9, 10, 11, 12]])

m.T
# displays the following result:
# array([[ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11],
#        [ 4,  8, 12]])

# NumPy does this without actually moving any data in memory - it simply changes 
# the way it indexes the original matrix - so it's quite efficient.
# 
# However, that also means you need to be careful with how you modify objects, 
# because they are sharing the same data. For example, with the same matrix m 
# from above, let's make a new variable m_t that stores m's transpose. Then look 
# what happens if we modify a value in m_t:

m_t = m.T
m_t[3][1] = 200
m_t
# displays the following result:
# array([[ 1,   5, 9],
#        [ 2,   6, 10],
#        [ 3,   7, 11],
#        [ 4, 200, 12]])

m
# displays the following result:
# array([[ 1,  2,  3,   4],
#        [ 5,  6,  7, 200],
#        [ 9, 10, 11,  12]])

# Notice how it modified both the transpose and the original matrix, too! 
# That's because they are sharing the same copy of data. So remember to consider 
# the transpose just as a different view of your matrix, rather than a different 
# matrix entirely.

# A real use case
# I don't want to get into too many details about neural networks because you 
# haven't covered them yet, but there is one place you will almost certainly 
# end up using a transpose, or at least thinking about it.
inputs = np.array([[-0.27,  0.45,  0.64, 0.31]])
inputs
# displays the following result:
# array([[-0.27,  0.45,  0.64,  0.31]])

inputs.shape
# displays the following result:
# (1, 4)

weights = np.array([[0.02, 0.001, -0.03, 0.036], \
    [0.04, -0.003, 0.025, 0.009], [0.012, -0.045, 0.28, -0.067]])

weights
# displays the following result:
# array([[ 0.02 ,  0.001, -0.03 ,  0.036],
#        [ 0.04 , -0.003,  0.025,  0.009],
#        [ 0.012, -0.045,  0.28 , -0.067]])

weights.shape
# displays the following result:
# (3, 4)

# I won't go into what they're for because you'll learn about them later, 
# but you're going to end up wanting to find the matrix product of these two matrices.
# If you try it like they are now, you get an error:

# np.matmul(inputs, weights)
# displays the following error:
# ValueError: shapes (1,4) and (3,4) not aligned: 4 (dim 1) != 3 (dim 0)
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0,
# with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 3 is different from 4)


# If you did the matrix multiplication lesson, then you've seen this error before. 
# It's complaining of incompatible shapes because the number of columns in the 
# left matrix, 4, does not equal the number of rows in the right matrix, 3.
# So that doesn't work, but notice if you take the transpose of the weights matrix, it will:
np.matmul(inputs, weights.T)
# displays the following result:
# array([[-0.01299,  0.00664,  0.13494]])

# It also works if you take the transpose of inputs instead and swap their order, 
# like we showed in the video:

np.matmul(weights, inputs.T)
# displays the following result:
# array([[-0.01299],# 
#        [ 0.00664],
#        [ 0.13494]])

# The two answers are transposes of each other, so which multiplication you use 
# really just depends on the shape you want for the output.

# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    print(inputs)
    print(type(inputs))
    print(np.array(inputs))
    input_array = np.array(inputs).reshape(1, len(inputs))
    
    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    inputs_minus_min = input_array - input_array.min()
    
    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    inputs_div_max = inputs_minus_min / inputs_minus_min.max()
    
    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max


def multiply_inputs(m1, m2):
    # TODO: Check the shapes of the matrices m1 and m2. 
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose
    print(m1.shape)
    print(m2.shape)
    inner_dim_m1 = m1.shape[1]
    outer_dim_m2 = m2.shape[0]
    inner_dim_m2 = m2.shape[1]
    outer_dim_m1 = m1.shape[0]
    print(inner_dim_m1, outer_dim_m2, inner_dim_m2, outer_dim_m2)
    # if we don't have the same dims on the inside when mult m1 x m2
    # or m2 x m1 then return false
    if (inner_dim_m1 != outer_dim_m2) & (inner_dim_m2 != outer_dim_m1):
        return False
    
    # TODO: If you have not returned False, then calculate the matrix product
    #       of m1 and m2 and return it. Do not use a transpose,
    #       but you swap their order if necessary
    if (inner_dim_m1 == outer_dim_m2):
        return np.matmul(m1, m2)
    else:
        return np.matmul(m2, m1)


def find_mean(values):
    # TODO: Return the average of the values in the given Python list
    arr_values = np.array(values)
    return arr_values.mean()


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1,2,7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print("Multiply 1:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3],[4]]))))
print("Multiply 2:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1],[2],[3]]))))
print("Multiply 3:\n{}".format(multiply_inputs(np.array([[1,2,3],[4,5,6]]), np.array([[1,2]]))))

print("Mean == {}".format(find_mean([1,3,4])))

m = np.array([[1,2,3],[4,5,6]])
print(m)

n = m * 0.25
print(n)


