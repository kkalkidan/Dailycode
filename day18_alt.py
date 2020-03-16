

"""
@Question

You are given an array of nonnegative integers. 
Let's say you start at the beginning of the array 
and are trying to advance to the end. You can advance at most, 
the number of steps that you're currently on. 

Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

Alternative solution based on @vineetjohns solution
https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_192.py

But this solution returns None when the end is unreachable


"""


def can_reach_end(steps):
    if(len(steps) < 2): return True

    for i in range(2, len(steps)):
        """
        this checks if we can take atleast i-1 steps from len(steps) -1 
        for example given [1, 3, 1, 2, 0, 1] the first iteration checks if 
        we can take at least one step from the 4th index position
        """
        if(steps[len(steps)-i]  >= i-1):
            return can_reach_end(steps[:len(steps)-i])
    
    return False

assert can_reach_end([1, 3, 1, 2, 0, 1])
assert not can_reach_end([1, 0, 3]) 
assert not can_reach_end([1, 2, 1, 0, 0])