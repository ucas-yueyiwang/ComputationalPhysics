import math
i = 1
Pn = 1
pn = 0
while Pn-pn > 1e-8:
    pn = 0.5 * math.sin(math.pi / 2 / i) * 2 * 2 * i
    Pn = 0.5 * math.tan(math.pi / 2 / i) * 2 * 2 * i
    i += 1

print(i)
print(Pn)
