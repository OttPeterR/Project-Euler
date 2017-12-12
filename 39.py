# given the perimeter, return how many integer right
# triangles are possible
# sad BFA :(
def triangles(p):
    validPerims = 0
    for a in range(1,p-2):
        for b in range(a, p-2):
            c = (a**2 + b**2)**0.5
            if a+b+c==p and c%1==0:
                validPerims += 1
    return validPerims

maxNumOfPs = 0
perim = 1
for p in range(1000):
    newNumOfPs = triangles(p)
    if newNumOfPs > maxNumOfPs:
        maxNumOfPs = newNumOfPs
        perim = p
print("perim: %d" % perim)
print("num of perims: %d" % maxNumOfPs)
