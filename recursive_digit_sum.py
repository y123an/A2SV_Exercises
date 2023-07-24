#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def calc(num):
    if num >=0 and num <= 9:
        return num
    
    sum = 0
    
    while num > 0:
        sum += num%10
        num = num//10
    
    return calc(sum)

def superDigit(n, k):
    # Write your code here
    
    num = 0
    
    for x in n:
        num += int(x)
    
    num *= k

    return calc(int(num))
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()