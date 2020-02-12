"""
@Question 
Given a 32-bit integer, return the number 
with its bits reversed.
For example, given the binary number 
1111 0000 1111 0000 1111 0000 1111 0000, 
return 0000 1111 0000 1111 0000 1111 0000 1111
"""

def reversed(bits):
    ones = '1'*len(bits)
    rev = int(ones, 2) ^ int(bits, 2)
    return format(rev, '0{}b'.format(len(bits)))



assert reversed('1111') == '0000', "Error"
assert reversed('0000') == '1111', "Error"
assert reversed('0101') == '1010', "Error"

"""
Solution Explanation:
    
Computing XOR operation between the bits and all 1's in the 
length of the bits, gives us the reverse

"""



