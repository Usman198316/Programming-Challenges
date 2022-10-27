def main():
    validStart = False
    n = int(input("Please enter the order of your latin square >> "))
    start = validateStart(validStart, n)
    position = numLoop(start, n)
    for i in range(1, n - position):
        numLoop(start + i, n)
    if position != 0:
        for i in range(1,n-position):
            numLoop(i, n)

    

def validateStart(validStart, n):
    while validStart == False:
        try:
            topleft = int(input("Please input the top left number >> "))
            if topleft not in range(1, n):
                raise exception
            else:
                validStart = True
        except:
            print("Not valid")

    return topleft
    
def numLoop(start, n,):
    
    dif = n - start
    nList = [x for x in range(1,n+1)]
    pos = nList.index(start)
    for i in range(pos, n):
        print(f'{nList[i]} ', end="")
    for i in range(0, pos):
        print(f'{nList[i]} ', end="")
    print("")
    return pos
    




   
main()


            
