#!/usr/bin/python3
import sys
factor2 = __import__('factoring2').factor2
allNumbers = open(sys.argv[1], 'r')
while True:
    number = allNumbers.readline()
    if number:
        factor2(int(number))
    else:
        break
allNumbers.close()
