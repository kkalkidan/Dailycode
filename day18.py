

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

"""

def can_reach_end(steps, current=0):
    # return true when already at the end or c
    next = current + steps[current]
    if(current >= len(steps)-1 or 
        next >= len(steps)-1): return True
    if(steps[current] == 0): return False

    while(next > current and (not can_reach_end(steps, next))):
        next-=1
    if(next == current): return False
    return True
    
assert can_reach_end([1, 3, 1, 2, 0, 1])
assert not can_reach_end([1, 0, 3]) 
assert not can_reach_end([1, 2, 1, 0, 0])