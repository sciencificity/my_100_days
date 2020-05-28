A = [2, 16, 26, 32, 52, 71, 80, 88]

# These are already sorted:
assert A == sorted(A)

def contains(A, x):
    """Returns True only if the value `x` exists in `A`."""
    return x in A

# print("A contains 32: {}".format(contains(A, 32)))
# print("A contains 7: {}".format(contains(A, 7)))
# print("A contains -10: {}".format(contains(A, -10)))


def ordered_contains(S, x):
    # You may assume that `S` is sorted
    last_ind = len(S) - 1
    mid = int(last_ind/2)
    if (x < S[0]):
        ret_val = False
        print(f'entered x < S[0] with x = {x} and S[0] = {S[0]}')
    elif (x == S[0]):
        ret_val = True
        print(f'entered x == S[0] with x = {x} and S[0] = {S[0]}')
    elif (x > S[-1]):
        ret_val = False
        print(f'entered x > S[-1] with x = {x} and S[-1] = {S[-1]} and {x>S[-1]}')
    elif (x == S[-1]):
        ret_val = True
        print(f'entered x == S[-1] with x = {x} and S[-1] = {S[-1]}')
    elif (x == S[mid]):
        ret_val = True
        print(f'entered x == S[mid] with x = {x} and S[mid] = {S[mid]} and mid = {mid}')
    elif ((x > S[mid]) and (mid > 0)):
        print(f'entered x > S[mid] with x = {x} and S[mid] = {S[mid]} and mid = {mid}')
        A = S[mid+1:]
        return ordered_contains(A, x)
    elif ((x < S[mid]) and (mid > 0)):
        print(f'x is {x}, and S[mid] is {S[mid]} and x < S[mid] is {x < S[mid]}')
        print(f'mid is {mid} and mid > 0 is {mid > 0}')
        B = S[:mid]
        print(f'B is {B}')
        return ordered_contains(B, x)
    else:
        ret_val = False
    
    if ret_val:
        print('ok')
    else:
        print('what is up!?!?')
        print(ret_val)
    return ret_val

print(ordered_contains(A, 7))

#print("A contains 32: {}".format(ordered_contains(A, 32)))
print("A contains 7: {}".format(ordered_contains(A, 7)))
#print("A contains -10: {}".format(ordered_contains(A, -10)))
# print("\n(Did those results match the earlier example?)")
S = [9, 26, 41, 47, 52, 57, 73, 74, 76, 91, 93, 94, 96]

# print(ordered_contains(S, S[0]), contains(S, S[0]))
# print(ordered_contains(S, S[0]-1), contains(S, S[0]-1))
# print(ordered_contains(S, S[-1]), contains(S, S[-1]))
# print(ordered_contains(S, S[-1]+1), contains(S, S[-1]+1))
# print(ordered_contains(S, 41), contains(S, 41))
        
def test_elif():
    var = 150
    if var == 200:
       print ("1 - Got a true expression value")
       return True
    elif var == 150:
       print ("2 - Got a true expression value")
       return False
    elif var == 100:
       print ("3 - Got a true expression value")
       return True
    else:
       print ("4 - Got a false expression value")
       return False
    
    print("Good bye!")
    
# print(test_elif())
