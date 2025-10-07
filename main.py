from math import *

primes = []

testing = 2
for i in range(500):
    trying = 2
    prime = True
    while trying <= sqrt(testing):
        if testing%trying == 0:
            prime = False
            #print(f'{testing} not prime with {trying}')
        trying += 1
    if prime == True:
        primes.append(testing)
    testing += 1 
print(primes)
