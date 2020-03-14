

"""
@Question
Given a collection of intervals, find the minimum number of intervals you need to remove 
to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can
be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.

"""

def min_removable_overlaps(intervals):
    # to count the number of overlaps
    overlaps = 0
    #sorting the intervals based on the starting number
    sorted_intervals = sorted(intervals, key=lambda k: k[0])
    for i in range(len(sorted_intervals)-1):
        if(sorted_intervals[i][1] > sorted_intervals[i+1][0]):
            overlaps+=1
    return overlaps


assert min_removable_overlaps([(7, 9), (2, 4), (5, 8)]) == 1
assert min_removable_overlaps([(7, 9), (2, 4)]) == 0

"""
@Solution
- Sort the intervals based on the starting number
- Iterate and increment overlaps when two consecuative intervals overlap

"""