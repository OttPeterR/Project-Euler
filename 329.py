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


def start_pad(pad, hops):
    if(hops == 15):
        return 0 # return something
    down_pad = pad - 1
    if down_pad == 0: # lower limit
        down_pad == 2
    up_pad = pad + 1
    if up_pad == 501: # upper limit
        up_pad = 499



    # something involving the current pad number
    # something recursive, might look like this:
    # start_pad(up_pad, hops+1 + start_pad(down_pad, hops+1)

for i in range(1,501):
    start_pad(0)
