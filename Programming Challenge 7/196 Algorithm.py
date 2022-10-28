def main():
    num1 = int(input("Integer 1 >> "))
    num2 = int(input("Integer 2 >> "))
    lychList = []
    nonLychList = []
    rangeList = [x for x in range(num1, num2 + 1)]
    numList = originalList(num1, num2, rangeList)
    palindromeList = findPalindromes(numList)
    for number in range(num1, num2+1):
        if isLych(number) == True:
            lychList.append(number)
        elif isLych(number) == False:
            nonLychList.append(number)
    for x in nonLychList:
        if x in palindromeList:
            nonLychList.remove(x)

    for number in lychList:
        print(f"{number} is probably lychrel")

    print(f"Palindrome numbers = {len(palindromeList)}")
    print(f"Not Lychrel numbers = {len(nonLychList)}")
    print(f"Lychrel = {len(lychList)}")


def wholenum(intList):
    wholeNum = ""
    for i in intList:
        wholeNum += i
    return wholeNum


def reverseNum(num):
    num = str(num)
    reverseNum = int(num[::-1])
    return reverseNum


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
            palindromes.append(int(wholenum(num)))
    return (palindromes)


def isLych(num):
    total = num
    reversedTotal = reverseNum(num)
    for i in range(0, 60):
        if checkPalindrome(total, reversedTotal) == True:
            return False
        else:
            total += reversedTotal
            reversedTotal = reverseNum(total)

    if checkPalindrome(total, reversedTotal) == False:
        return True



def checkPalindrome(num, reverseNum):
    if num == reverseNum:
        return True
    else:
        return False


main()

