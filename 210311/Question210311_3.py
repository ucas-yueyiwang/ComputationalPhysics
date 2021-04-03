bignum = 2**1000
mysum = 0
while bignum > 0:
    mysum += bignum % 10
    bignum = bignum // 10
print(mysum)
