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

def getPrime(prime_num):

    num = 2
    prime_count = 0
    curr_prime = 2

    while prime_count < prime_num:
        if isPrime(num):
            curr_prime = num
            prime_count += 1
        num += 1
    return curr_prime

print(getPrime(10001))
