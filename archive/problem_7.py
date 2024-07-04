# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?


n = 2
primes = []

def is_prime(n):
    factors = []
    for i in range(1, n + 1):
        if (n % i == 0):
            factors.append(i)
    return len(factors) <= 2

while len(primes) < 10001:
    if (is_prime(n)):
        primes.append(n)
    n = n + 1

print(primes)
