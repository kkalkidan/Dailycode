"""
You are given a starting state start, a list of transition probabilities for a Markov chain,
and a number of steps num_steps. Run the Markov chain starting from start for num_steps and
compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition 
probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
"""
import numpy as np

def markov_chain(prob_list, state, num_steps):

  length = len(state)

  state = np.array(state).reshape(1, length)
  prob_matrix = np.zeros((length, length))

  for i in range(length):
    for j in range(length):
      prob_matrix[i][j] = prob_list[(i*length) + j][2]
  for i in range(num_steps):
    prev_state = state
    state = np.dot(state, prob_matrix)
    if(np.sum(state == prev_state) == length):
      print("Converges after ", i, "runs.")
      break
   

  return state * num_steps



print(markov_chain(
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
],
[1, 0, 0],
5000))

"""
Reference video on Markov's chain : https://www.youtube.com/watch?v=Uz3JIp6EvIg

"""