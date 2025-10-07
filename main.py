from math import *

primes = []

testing = 2
while True:
    trying = 2
    prime = True
    while trying <= sqrt(testing):
        if testing/trying != 0:
            prime = False
        trying += 1
    if prime == True:
        primes.append(testing)
    testing += 1 
    print(primes)
    
