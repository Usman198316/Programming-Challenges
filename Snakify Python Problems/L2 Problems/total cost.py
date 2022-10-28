a = int(input("Enter the number of dollars a cupcake costs:"))
b = int(input("Enter the number of cents a cupcake costs:"))
n = int(input("How many cupcakes are there?"))

b = b/100
cost = a + b
totalcost = n*cost
totaldollars = int(totalcost // 1)
totalcents = (totalcost - totaldollars)*100
totalcents = round(totalcents)
print(totaldollars, totalcents)
