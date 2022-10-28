n = int(input("Enter the number of kilometres the car can travel per day?"))
m = int(input("How many kilometres long is the route that the car can take?"))
num = m/n
wholenum = num // 1
fraction = num - wholenum
if fraction > 0:
    wholenum = wholenum + 1
    
print(int(wholenum))
