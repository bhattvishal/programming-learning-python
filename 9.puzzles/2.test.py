#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    result = 0
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    

if __name__ == '__main__':
    
    print(fizzBuzz(15))