#----------print twin primes less than 1000----------
def isprime(no)

def tPrimes(n):
    for i in range (0,len(n)):
        if (isprime(i) == True and isprime(i+1) ==True):
            print(i," : ",i+1)

tPrimes(1000)