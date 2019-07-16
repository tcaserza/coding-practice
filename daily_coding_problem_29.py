# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
# successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded
# as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
# solely of alphabetic characters. You can assume the string to be decoded is valid.


def run_length_encode(s):
    count = 1
    last_c = s[0]
    output = ""
    for i in range(1,len(s)):
        if s[i] == last_c:
            count += 1
        else:
            output += str(count) + last_c
            last_c = s[i]
            count = 1
    output += str(count) + last_c
    return output


def run_length_decode(s):
    output = ""
    for c in range(0,len(s),2):
        for i in range(int(s[c])):
            output += s[c+1]
    return output

initial_string = "AAAABBBCCDAA"
encoded_string = run_length_encode(initial_string)
decoded_string = run_length_decode(encoded_string)
print "initial string: %s" % initial_string
print "encoded string: %s" % encoded_string
print "decoded string: %s" % decoded_string
