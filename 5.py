n = 20
primes = []
factors = []
ans = 1
for i in range(2,n+1):
    new = True
    for j in range(len(primes)):
        if  not (i % primes[j]):
            new = False
            new_factor = factors[j]
            while not (i % new_factor):
                factors[j] = new_factor
                new_factor *= primes[j]
    
    if new:
        primes.append(i)
        factors.append(i)

ans = 1
for f in factors:
    ans *= f
print(ans)