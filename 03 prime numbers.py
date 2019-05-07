primes = []


for primeNumbers in range (2, 995): #range 2-500 only
    isPrime = True
    for number in range(2, primeNumbers):
        if primeNumbers % number == 0:
            isPrime = False
    
    if isPrime:
        primes.append(primeNumbers)
        
    #print(primes)
    
primeNumbers

print(primes[-1]) #will show the largest Prime number 