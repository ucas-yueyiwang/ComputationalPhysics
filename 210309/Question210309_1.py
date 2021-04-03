temp1 = 1.0
temp2 = 1.0
buffer = 0.0
phi = (1+5**0.5)/2
i = 2

while abs(temp1/temp2-phi) > 1e-10:
    i = i+1
    buffer = temp1+temp2
    temp2 = temp1
    temp1 = buffer
    print(i, temp1)
print(i)
print(temp1/temp2-phi)
