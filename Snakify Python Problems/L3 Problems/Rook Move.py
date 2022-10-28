colum1 = int(input())
row1 = int(input())
colum2 = int(input())
row2 = int(input())
if (row2 == (row1 + 1) or (row1 - 1)) and colum1 == colum2:
    print("YES")
elif (colum2 == (colum1 + 1) or (colum1 - 1)) and row1 == row2:
    print("YES")
else:
    print("NO")

