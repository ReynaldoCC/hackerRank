#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    input_format = '%I:%M:%S%p'
    output_format = '%H:%M:%S'
    received_time = time.strptime(s, input_format)
    return time.strftime(output_format, received_time)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
