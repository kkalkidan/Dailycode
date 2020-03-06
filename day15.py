"""
@Question
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
"""

def GCD(array):
    gcd = 1
    for i in range(len(array)):
        found = True
        current = array[i]
        for j in range(len(array)):
            if(array[j] % array[i] != 0):
                found = False
                break
        if(found and current > gcd): gcd = current      
    
    return gcd 

assert GCD([42, 56, 14]) == 14
# No GCD except 1
assert GCD([13, 56, 14]) == 1 