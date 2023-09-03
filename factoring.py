#!/bin/usr/python3
import math
def factor(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            print(f"{n}={n // i}*{i}")
            break
