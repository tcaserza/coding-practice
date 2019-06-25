# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].


def DoWork(int_array):
    total_product = 1
    new_array = []
    for i in int_array:
        total_product *= i
    for i in range(len(int_array)):
        new_array.append(total_product/int_array[i])
    return new_array

array = [1,2,3,4,5]
print "%s -> %s" % (array, DoWork(array))
array = [2,3,6]
print "%s -> %s" % (array, DoWork(array))


