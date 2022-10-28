def main():
    num1 = int(input("Integer 1 >> "))
    num2 = int(input("Integer 2 >> "))
    rangeList = [x for x in range(num1, num2+1)]
    numList = originalList(num1, num2, rangeList)
    palindromeList = findPalindromes(numList)
    findLychrel(rangeList, numList)
    
def wholenum(intList):
    wholeNum = ""
    for i in intList:
        wholeNum += i
    return wholeNum

##    for i in list:
##        wholenum = ""
##        for j in i:
##            wholenum += j
##        return(wholenum)
        
    
def originalList(num1, num2, numList):
    original = []
    digList = []
    for i in numList:
        number = str(i)
        for digit in number:
            digList.append(digit)
        original.append(digList)
        digList = []
    return original

def findPalindromes(original):
    palindromes = []
    for num in original:
        if num[::-1] == num:
            palindromes.append(num)
    return(palindromes)
            
        
def findLychrel(rangeList, numList):
    lychrel = True
    count = 0
    total = 0
##    num = int(wholenum(numList[count]))
    num = 262
    for i in range(0, 60):
        reversedNum = reverseNum(num)
        if reversedNum == num:
            lychrel = False
            count += 1
            print(num)
        else:
            total = num + reversedNum
            num = total
            
        

        
        
        
##    while lychrel == True and count <= 60:
##        num = numList[count]
##        lychrel = checkEqual(num)
##        if lychrel == True:
##            count+=1
            
            
def reverseNum(num):
    num = str(num)
    reverseNum = int(num[::-1])
    return reverseNum

        

    lychrel = False
        
def checkEqual(num):
    reversedNum = num[::-1]
    if reversedNum == num:
        return False
    else:
        return True
    
    
    
    
    
            
            
    
    

main()
