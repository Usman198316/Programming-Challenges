colum1 = int(input())
row1 = int(input())
colum2 = int(input())
row2 = int(input())
numofsquares = colum2 - colum1
if colum1 + numofsquares == colum2 and (row1 + numofsquares == row2 or row1 - numofsquares == row2 :
    print("YES")
else:
    print("NO")
