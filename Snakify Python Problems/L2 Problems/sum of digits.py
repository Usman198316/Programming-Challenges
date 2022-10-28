validnum = False
while validnum == False:
    num = int(input("Enter a 3 digit number :"))     #Input and validation check
    if num < 100 or num > 999 :
        print("That is not a 3 digit number")
        validnum = False
    else:
        validnum = True

num = str(num)                                       #Calculates sum of digits
digit1 = int(num[0])
digit2 = int(num[1])
digit3 = int(num[2])
total = digit1 + digit2 + digit3
print("The sum of the digits of " + num + " is " + str(total))



    
    
