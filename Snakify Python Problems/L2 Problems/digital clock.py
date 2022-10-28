n = int(input("How many minutes have passed since midnight"))
numhours = int(n/60)
numMins = n - (numhours*60)
print(str(numhours) + " " + str(numMins))
