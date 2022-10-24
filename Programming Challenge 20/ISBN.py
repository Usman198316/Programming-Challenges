def ISBN():
    ISBN = str(input("Please enter a valid ISBN with a single missing digit, marked with a '?' >> "))
    pos_val = int(ISBN.find("?"))
    total = findTotal(ISBN)
    missingVal = findMissingVal(ISBN, pos_val, total)
    print(missingVal)
    

def findTotal(ISBN):
    total = 0
    count = 10
    for char in ISBN:
        if char not in ["X", "?"]:
            total += (count * int(char))
        elif char == "X":
            total += 10
        count -= 1
          
    return total

def findMissingVal(ISBN, pos_val, total):
    for i in range(0, len(ISBN)+1):
        if ((total + ((10-pos_val)*i)) % 11) == 0:
            missingVal = i
    if missingVal == 10:
        missingVal = "X"
    return missingVal

ISBN()

    
