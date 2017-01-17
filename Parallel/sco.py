#!/usr/bin/env python3
from scoop import futures

data = [[i for i in range(x, x + 1000)] for x in range(0, 8001, 1000)]


def mySum(inIndex):
    """The worker will only receive an index from network."""
    return sum(data[inIndex])

if __name__ == '__main__':
    results = list(futures.map(mySum, range(len(data))))

# #from __future__ import print_function
# from scoop import futures
# import time

# def helloWorld(value):
#     time.sleep(1)
#     return "Hello World from Future #{0}".format(value)

# if __name__ == "__main__":
#     returnValues = list(  futures.map(helloWorld, range(16))   ) 
#     print("\n".join(returnValues))
