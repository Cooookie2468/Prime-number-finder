from math import *

primes = []
notPrimes = {}

for testing in range(2,int(input('what number do you want find primes below? '))):
    prime = True
    for trying in range(2,ceil(sqrt(testing))):
        if testing%trying == 0:
            prime = False
            notPrimes[trying].append(testing)
            break
    if prime == True:
        primes.append(testing)
        notPrimes[testing]=[]
print(f'primes:\n{primes}')
print(f'not primes and what they are first divisable by:\n{notPrimes}')
