sum = 0
cur = 1
prev = 0
while cur < 4000000:
    temp = prev
    prev = cur
    cur += temp
    if(cur%2==0):
        sum += cur
print sum
