from math import *

primes = []

trying = 1
while True:
    testing = 1
    prime = True
    while trying < sqrt(testing):
        if testing/trying != 0:
            prime = False
        trying += 1
    if prime == True:
        primes.append(testing)
    trying += 1 
    print(primes)
    
