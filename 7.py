# returns True if n is prime, False otherwise
def is_prime(n):
    # using the AKS method of prime verification
    if n==2 or n==3:
        return True
    elif n%2==0 or n%3==0 or n<2:
        return False
    i,w = 5,2
    while i*i<=n:
        if n%i==0:
            return False
        i+=w
        w=6-w
    return True

primes = 0
count = 2
while primes != 10001:
    if(is_prime(count)):
        primes += 1
    count += 1
count -= 1
print(count)
