def main():
    romanNumeralDict = {"C": 100,"XC": 90,"L": 50,"XL":40,"IX":9, "X": 10, "V": 5,"IV":4, "I": 1}
    romanNum1 = str(input("Please enter the first Roman Number (no spaces) >> "))
    digitalNum1 = subtractionRule(getValueList(romanNum1, romanNumeralDict))
    print(f"Value of {romanNum1} >> {digitalNum1}")
    romanNum2 = str(input("Please enter the second Roman Number (no spaces) >> "))
    digitalNum2 = subtractionRule(getValueList(romanNum2, romanNumeralDict))
    print(f"Value of {romanNum2} >> {digitalNum2}")
    digitalSum = digitalNum2 + digitalNum1
    print(f"Digital sum is >> {digitalSum}")
    numeralSum = listToString(getRomanNumeral(digitalSum, romanNumeralDict))
    print(f"Roman sum is >> {numeralSum}")

    print()
    input("Press enter to quit >> ")


def getValueList(romanNum, romanNumeralDict):
    digitalValueList = []
    for char in romanNum:
        if char in romanNumeralDict:
            digitalValueList.append(romanNumeralDict[char])
    return digitalValueList


def subtractionRule(digitalValueList):
    totalValue = 0
    for i in range(0, len(digitalValueList)-1):
        if digitalValueList[i] < digitalValueList[i+1]:
            digitalValueList[i] = digitalValueList[i+1]-digitalValueList[i]
            totalValue += digitalValueList[i]
            totalValue -= digitalValueList[i+1]
        else:
            totalValue += digitalValueList[i]
    totalValue += digitalValueList[-1]
    return totalValue


def getRomanNumeral(num, romanNumeralDict):
    numeralList = []
    for i in romanNumeralDict:
        while num >= romanNumeralDict[i]:
            num -= romanNumeralDict[i]
            numeralList.append(i)
    return numeralList


def listToString(list):
    mystr = ""
    for i in list:
        mystr += str(i)
    return mystr


main()
