#ifelse problem


#!/bin/python3

import math
import os
import random
import re
import sys


def iseven(n):
    if n % 2 == 0 :
        return True


if __name__ == '__main__':
    #strip is used to strip out the unwanted white spaces 
    n = int(input().strip())

    if n <= 100 and n >=1:
        if not(iseven(n)):
            print("Weird")
        elif (iseven(n)) and n in range(2,6):
            print("Not Weird")
        elif (iseven(n)) and n in range(6,21):
            print("Weird")
        elif (iseven(n)) and n > 20 :
            print("Not Weird")



            """ Here is the explanation for the code above:
1. first we take input from the user and convert it to integer
2. then we check if the input is between 1 and 100
3. then we check if the number is not even and print "Weird" if it is not even
4. if the number is even we check if it is between 2 and 5 and print "Not Weird" if it is
5. if the number is even we check if it is between 6 and 20 and print "Weird" if it is
6. if the number is even we check if it is greater than 20 and print "Not Weird" if it is """


