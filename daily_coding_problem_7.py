# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.


def num_ways(message):
    if len(message) < 2:
        return 1
    ways = 0
    if int(message[:2]) <= 26:
        ways += num_ways(message[2:])
    ways += num_ways(message[1:])
    return ways


print num_ways("1111")

