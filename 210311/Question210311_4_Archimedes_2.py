import math
n = 3
pn = 0.5*math.sin(math.pi/n)*2*n
Pn = 0.5*math.tan(math.pi/n)*2*n

print(pn, Pn)
print("pn=Pn*cos(pi/2n)")
while Pn-pn > 1e-8:
    n *= 2
    Pn = 2*pn*Pn/(pn+Pn)
    pn = (pn*Pn)**0.5

print(Pn, pn, n)


