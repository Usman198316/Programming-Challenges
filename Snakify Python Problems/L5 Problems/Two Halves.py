import math
s = str(input())
slen = len(s)
halflen = math.ceil(slen / 2)
half1 = s[0 : halflen]
half2 = s[halflen : ]
print(half2, half1, sep = "")

