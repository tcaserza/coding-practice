# The area of a circle is defined as pi*r^2. Estimate pi to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x^2 + y^2 = r^2.
import math
import random


def create_point():
    x = float(random.randint(0,100)) /100
    y = float(random.randint(0,100)) /100
    return is_in_circle(x,y)


def is_in_circle(x,y):
    if math.pow(x,2) + math.pow(y,2) < 1:
        return True
    else:
        return False


in_circle_count = 0
total_count = 0
for i in range(0,10000):
    total_count += 1
    if create_point():
        in_circle_count += 1

print (float(in_circle_count) / float(total_count)) * 4