# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number
# of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
from collections import defaultdict


def find_min_rooms(t_array):
    times = defaultdict(int)
    for t in t_array:
        for time in range(t[0],t[1]):
            times[time] += 1
    rooms = 0
    for k,v in times.iteritems():
        if v > rooms:
            rooms = v
    return rooms

print find_min_rooms([(30, 75), (0, 50), (60, 150)])