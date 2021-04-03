i = 100
j = 100
buffer = 0
res = 0
while i <= 999:
    j = 100
    while j <= 999:
        buffer = i*j
        # print(i)
        if str(buffer) == str(buffer)[::-1]:
            if buffer > res:
                res = buffer
        j += 1
    i += 1

print(res)
