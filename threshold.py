'''
Write a function threshold(values, goal) that behaves as follows.
The first parameter is a sequence of numbers. The second parameter is a
single positive number. The function is to return the smallest possible
integer n such that the sum of the first n numbers in the sequence is
greater than or equal to goal. For example, threshold([5, 3, 8, 2, 9, 1],
17) should return 4 because the goal can be achieved by the sum of the
first four values (5+3+8+2).
If the goal is unachievable, the function should return 0.
'''

def threshold(values, goal):
  partials = 0
  for x in values:
    partials += x
    if partials >= goal:
      return x
  return 0

