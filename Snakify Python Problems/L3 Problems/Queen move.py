colum1 = int(input())
row1 = int(input())
colum2 = int(input())
row2 = int(input())
numofsquares = colum2 - colum1

if (row2 == (row1 + 1) or (row1 - 1)) and colum1 == colum2:
    print("YES")
elif (colum2 == (colum1 + 1) or (colum1 - 1)) and row1 == row2:
    print("YES")
elif colum1 + numofsquares == colum2 and (row1 + numofsquares == row2 or row1 - numofsquares == row2):
    print("YES")
else:
    print("NO")
