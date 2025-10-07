from math import *

primes = []
notPrimes = {}

testing = 2
for i in range(500):
    trying = 2
    prime = True
    while trying <= sqrt(testing):
        if testing%trying == 0:
            prime = False
            notPrimes[trying].append(testing)
            break
        trying += 1
    if prime == True:
        primes.append(testing)
        notPrimes[testing]=[]
    testing += 1 
print(primes)
print(notPrimes)
    
