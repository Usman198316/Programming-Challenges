s = str(input())
f = ""
for i in range(0, len(s)):
    if i % 3 != 0:
        f = f + s[i]
print(f)
    
