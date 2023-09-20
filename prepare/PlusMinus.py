#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    zero_counter = positive_counter = negative_counter = number_items = 0
    len(arr)
    for item in arr:
        if item > 0:
            positive_counter += 1
        elif item < 0:
            negative_counter += 1
        else:
            zero_counter += 1
        number_items += 1

    print(f'{positive_counter/number_items:.6f} \n{negative_counter/number_items:.6f} \n{zero_counter/number_items:.6f} ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
