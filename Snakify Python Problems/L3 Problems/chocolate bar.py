n = int(input())
m = int(input())
k = int(input())
if n == 1 or k == 1 or m == 1:
    print("NO")
elif k > m*n:
    print("NO")
elif k % n == 0 or k % m == 0:
    print("YES")
else:
    print("NO")

