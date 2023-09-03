#!/bin/usr/python3
import math
isPrime = __import__('isPrime').isPrime
def factor2(n):
    count = 0
    if n < 2:
        print(f"{n}=1*{n}")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if isPrime(i) and isPrime(n // i):
                print(f"{n}={n // i}*{i}")
                count += 1
                break
            continue
    if count == 0:
        print(f"{n}={n}*1")
