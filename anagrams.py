#
# Problem: Determine if a string is an anagram
#

def check_anagram(mystring):
    mystring_length = len(mystring)
    for i in range(mystring_length/2):
        if mystring[i] != mystring[mystring_length - i - 1]:
            return False
    return True


print check_anagram("aabaa")

