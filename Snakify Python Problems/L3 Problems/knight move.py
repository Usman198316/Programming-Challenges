colum1 = int(input())
row1 = int(input())
colum2 = int(input())
row2 = int(input())
if abs((colum2 - colum1)) == abs(2*(row2 - row1)) or abs((colum2 - colum1)) == abs(0.5*(row2 - row1)):
    print("YES")
else:
    print("NO")
