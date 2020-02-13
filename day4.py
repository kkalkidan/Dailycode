"""
@Question 
Implement a stack API using only a heap. 
A stack implements the following methods:
- push(item), which adds an element to the stack
- pop(), which removes and returns the most
  recently added element (or throws an error 
  if there is nothing on the stack)

Recall that a heap has the following operations:
- push(item), which adds a new key to the heap
- pop(), which removes and returns the max value of the heap
"""

import sys
import heapq

class Stack:
    def __init__(self):
        self.heap = []
        self.count = sys.maxint
    def push(self, value):
        heapq.heappush(self.heap, (self.count, value))
        self.count -= 1
    def pop(self):
        return heapq.heappop(self.heap)


stack = Stack()

for i in [6, 4, 2, 5]:
    stack.push(i)

for i in [5, 2, 4, 6]:
    assert (i == stack.pop()[1]), "Error"

"""
Solution Explanation:
    
In the stack implementation, we push a key, value pair to the heap
and the heap acts us a priority queue where the highest priority is 
given to the element inserted last.

In this case, python's min-heap is used.

"""

