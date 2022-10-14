import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

try:
    operator = input("Please enter the operation you would like to perform >> ")
    num = int(input("Please enter a natural number >> "))
    if num < 0:
        raise ValueError
    elif operator not in "/*+-":
        raise TypeError
except ValueError:
    print("Please enter a natural number (must be greater than 0)")
except TypeError:
    print("Please enter a valid operator")



def table(operator, num):
    rows,columns = (num+1, num+1)
    table = [[0 for i in range(rows)]for j in range(columns)]
    firstRow = [x for x in range(rows)]
    firstRow = [str(i) for i in firstRow]
    print(f"{operator} {' '.rjust(0,' ').join(firstRow)} \n ------------")
    
    

    for i in range(rows):
        for j in range(columns):
            try:
                table[i][j] = (ops[operator](i, j))
                value = table[i][j]
            except ZeroDivisionError:
                table[i][j] = "-"
                value = table[i][j]
            finally:
                try:
                    print(f"{i} {round(table[i][j],1), end = ' '}")
                except:
                    print(f"{i} {table[i][j], end = ' '}")
        print("\n")
            

        
           
    
        
    
##    table = []
##    for x in range(0, num+1):
##        column = []
##        for y in range(0, num+1):
##            column.append(ops[operator](0, y))
##
##        table.append(column)
##    print(table)
         
    
##    for i in range(0, num+1):
##        for j in range(0, num+1):
##            print(ops[operator](0, i))


table(operator, num)
