#School Desks
from math import ceil

a = int(input("Enter the number of students in the first class:"))
b = int(input("Enter the number of students in the second class:"))
c = int(input("Enter the number of students in the third class:"))
aDesks = ceil(a / 2)
bDesks = ceil(b / 2)
cDesks = ceil(c / 2)
totalDesks = aDesks + bDesks + cDesks
print(ceil(totalDesks))
