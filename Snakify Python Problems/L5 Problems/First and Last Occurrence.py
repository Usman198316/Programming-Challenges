s = str(input())
slen = len(s)
f1 = int(s.find("f"))
f2 = int(s.rfind("f"))

if f1 == f2:
    if f1 != -1:
        f2 = str("")
    
if f1 == -1:
    f1 = str("")
    
if f2 == -1:
    f2 = str("")
    

print(f1, f2)
