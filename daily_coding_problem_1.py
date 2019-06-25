#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#

def DoWork(number_list,k):
    seen_list = []
    for number in number_list:
        if k - number in seen_list:
            return True
        else:
            if number not in seen_list:
                seen_list.append(number)
    return False

number_list = [10,15,3,7]
k = 17
print DoWork(number_list,k)