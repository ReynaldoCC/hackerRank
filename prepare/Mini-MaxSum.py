#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def give_me_sum(arr):
    return reduce(lambda x, y: x + y, arr)

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min_sum = give_me_sum(arr[:-1])
    max_sum = give_me_sum(arr[1:])
    print(f'{min_sum} {max_sum}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
