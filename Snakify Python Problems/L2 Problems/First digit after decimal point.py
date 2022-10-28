valid = False
while valid == False:
    num = float(input("Enter a positive real number:"))    #validation check for positive input
    if num < 0:
        print("That isn't a positive number!")
    else:
        valid = True

wholenum = num // 1
fraction = float(num - wholenum)
length = (str(fraction))
length = str(length)
decimal = length[2]
print(decimal)
