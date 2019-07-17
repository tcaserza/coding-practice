# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
# is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
# index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def compute_water(emap):
    total_water = 0
    wall_units = 0
    last_wall_height = emap[0]
    last_wall_location = 0
    for i in range(1, len(emap)):
        if emap[i] >= last_wall_height:
            total_water += (last_wall_height * (i-1 - last_wall_location)) - wall_units
            last_wall_height = emap[i]
            last_wall_location = i
            wall_units = 0
        else:
            wall_units += emap[i]

    return total_water


print "compute_water([3, 0, 1, 3, 0, 5]): %s" % compute_water([3, 0, 1, 3, 0, 5])
print "compute_water([2, 1, 2]): %s" % compute_water([2, 1, 2])
print "compute_water([3, 0, 1, 4, 0, 5]): %s" % compute_water([3, 0, 1, 4, 0, 5])




