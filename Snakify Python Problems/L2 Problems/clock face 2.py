a = float(input("Enter the number of degrees that the hour hand has turned since midnight"))
numMindegrees = a*12
numfullturns = numMindegrees // 360
numdegrees = numfullturns*360
numfinal = numMindegrees - numdegrees
print(numfinal)

