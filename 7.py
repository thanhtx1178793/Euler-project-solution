from datetime import datetime
import math
n = 10001

primes = []

num = 2
while len(primes) < n:
    k = int(math.sqrt(num))
    new = True
    for p in primes:
        if num % p == 0:
            new = False
            break
        if p > k:
            break
    if new:
        primes.append(num)
    num += 1
    
print(primes[-1])