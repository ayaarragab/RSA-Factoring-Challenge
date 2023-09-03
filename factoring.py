#!/bin/usr/python3
import math
def factor(n):
    if n < 2:
        print(f"{n}=1*{n}")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"{n}={n // i}*{i}")
            break
