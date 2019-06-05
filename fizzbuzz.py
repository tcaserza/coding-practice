#
# PROBLEM:
# Write a short program that prints each number from 1 to 100 on a new line.
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
#


def fizzbuzz():
    for i in range (1,100):
        if i % 3 == 0 or i % 5 == 0:
            line = ""
            if i % 3 == 0:
                line = "Fizz"
            if i % 5 == 0:
                line += "Buzz"
            print line
        else:
            print i

print fizzbuzz()
