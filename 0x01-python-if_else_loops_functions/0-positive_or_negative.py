#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number < 0:
     print('Negative')
elif number == 0:
    print('Zero')
elif number > 0:
    print('Positive')
