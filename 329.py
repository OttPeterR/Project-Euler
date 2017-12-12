goal = "PPPPNNPPPNPPNPN"

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


def start_pad(n):
    return 0


for i in range(1,501):
    start_pad(0)
