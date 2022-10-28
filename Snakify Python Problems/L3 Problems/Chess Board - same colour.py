colum1 = int(input())
row1 = int(input())
colum2 = int(input())
row2 = int(input())
c1 = colum1 + row1
c2 = colum2 + row2
if c1 % 2 == c2 % 2:
    print("YES")
else:
    print("NO")
