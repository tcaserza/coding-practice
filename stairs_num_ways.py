#
# PROBLEM: Given a number of stairs, and a list of allowed steps, determine the number of possible combination of
#          steps to reach the top.
#


def num_ways(steps,allowed_steps):
    global run_count
    ways = 0
    if steps in known_ways:
        return known_ways[steps]
    for i in allowed_steps:
        if steps > i:
            ways += num_ways(steps-i,allowed_steps)
        if steps == i:
            ways += 1
    known_ways[steps] = ways
    run_count += 1
    return ways

known_ways = {}
run_count = 0
print num_ways(4,[1,2,3]), run_count