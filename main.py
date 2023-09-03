#!/usr/bin/python3
import sys
factor = __import__('factoring').factor
allNumbers = open(sys.argv[1], 'r')
while True:
    number = allNumbers.readline()
    if number:
        factor(int(number))
    else:
        break
allNumbers.close()
