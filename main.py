from math import *

primes = []
notPrimes = {}

for testing in range(2,500):
    prime = True
    for trying in range(2,ceil(sqrt(testing))):
        if testing%trying == 0:
            prime = False
            notPrimes[trying].append(testing)
            break
    if prime == True:
        primes.append(testing)
        notPrimes[testing]=[]
print(primes)
print(notPrimes)
