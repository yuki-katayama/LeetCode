import math

x1 = str(121)
success = 1
for i in range(math.floor(len(x1) / 2)):
    print(x1[i], x1[-(i + 1)], i)
    if x1[i] != x1[-(i + 1)]:
        success = 0
        break
if (success == 1):
    print("true")
else:
    print("false")