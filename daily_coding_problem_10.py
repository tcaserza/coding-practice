# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
# Medium

import time


def scheduler(f,n):
    time.sleep(n/1000)
    return f()


print scheduler(lambda: "Hello World", 5000)