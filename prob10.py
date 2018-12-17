import atkin
import math

def isPrime(num):
    if num < 3:
        return False

    z = 3
    while math.ceil(math.sqrt(num)) > z:
        if num % z == 0:
            return False
        else:
            z += 1
    return True


def getPrimeSum(prime_num):

    #use the akin prime number sieve to generate a list of all primes below two million
    print("Generating Prime List....")
    prime_list = atkin.atkin_sieve(prime_num)
    print("Calculating Sum...")
    sum = 0
    for prime in prime_list:
        if not isPrime(prime):
            print("BROKE:",prime)
        else:
            sum += prime
    
    return sum

print(getPrimeSum(2000000))