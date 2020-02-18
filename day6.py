"""
@Question 
You are given n numbers as well as n probabilities
that sum up to 1. Write a function to generate one
of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and
probabilities [0.1, 0.5, 0.2, 0.2], your function 
should return 1 10% of the time, 2 50% of the time, 
and 3 and 4 20% of the time.
"""
import random

def random_generator(numbers, probabilities):
    # generate unifrom distributions from 0 to 1
    generated = random.uniform(0, 1)
    # returning sorted index of the probabilities 
    # Reference : https://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list
    prob_index = sorted(range(len(probabilities)), key=lambda k: probabilities[k])
    
    prev = 0
    for i in range(len(numbers)):
        upper = prev+probabilities[prob_index[i]]
        if(generated > prev  and generated < upper):
            return numbers[prob_index[i]]
        prev = upper

   
random_generator([1,2,3,4], [0.1,0.5,0.2,0.2])

"""
Solution Explanation:

Sorting the probabilities and comparing them with the result of the uniform random
distribution

For example if the above probabiliies array is sorted we will get
[0.1, 0.2, 0.2, 0.5]

accordingly the numbers array will change to [1, 3, 4, 2]

we will assign the following based on the return value of random uniform distribution

from 0 to 0.1 -> 1
from 0.1 to 0.3 -> 3
from 0.3 to 0.5 -> 4

"""

