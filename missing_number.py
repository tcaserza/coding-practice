#
# PROBLEM: Given a set of numbers as a string, find the missing number
#


def find_missing_number(number_string,max):
    numbers = set()
    for number in number_string.split():
        numbers.add(int(number))
    for i in range(1,max):
        if i not in numbers:
            return i


print(find_missing_number("5 4 6 3 2 1 8 9",9))


