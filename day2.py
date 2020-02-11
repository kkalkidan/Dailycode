"""
@Question 
Given a string, determine whether any permutation 
of it is a palindrome.
For example, carrace should return true, since it can
be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement 
that can form a palindrome.
"""

def is_palindrome(word):
    occurs_ones = []
    for char in word:
        if(char in occurs_ones):
            occurs_ones.remove(char)
        else: occurs_ones.append(char)

    return len(occurs_ones) < 2
    

assert is_palindrome("carrace"), "Error"
assert not is_palindrome("daily"), "Error"

"""
Solution Explanation:
    
A palindrome should have pairs of letters which are the same, 
and atmost a letter that doesn't have a pair

For example 'aba' is a palindrome, because there are a pair of 'a' and a single 'b'
However, 'abaa' is not a palindrome, because there is a single 'a' and 'b' that 
don't have pair.
"""