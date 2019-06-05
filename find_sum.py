#
# PROBLEM: Given an array of numbers, find two numbers in the array whose sum equals a given number
#


def find_sum(numbers,sum):
    for i in range(0,len(numbers)-1):
        if sum - numbers[i] in numbers:
            return numbers[i], sum - numbers[i]


print find_sum([1,2,3,4,5],9)