#
# PROBLEM: determine if word is a rotated palindrome
#



def is_palindrome(word):
    for i in range(0,len(word)/2):
        if word[i] != word[len(word) -1 - i]:
            return False
    return True

check_string = "BAABCC"
for i in range(0,len(check_string) -1):
    rotated_string = check_string[i:] + check_string[:i]
    if is_palindrome(rotated_string):
        print "%s is a rotated palindrome of %s" % (check_string, rotated_string)
