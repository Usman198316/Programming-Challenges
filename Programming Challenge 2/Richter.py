

def convJoules(richter):
  energy = 10 ** (1.5* float(richter) + 4.8)
  return energy

def convTNT(richter):
  energy = 10 ** (1.5* float(richter) + 4.8)
  TNT = energy / (4.184 * 10 ** 9)
  return TNT

print(f"Richter          Joules                              TNT \n 1          {convJoules(1)}                    {convTNT(1)} \n 5          {convJoules(5)}                    {convTNT(5)} \n 9.1          {convJoules(9.1)}                    {convTNT(9.1)} \n 9.2          {convJoules(9.2)}                    {convTNT(9.2)} \n 9.5          {convJoules(9.5)}                    {convTNT(9.5)}")
  
userValue = input("Please enter a Richter scale value: ")
print(f" Richter Value: {userValue} \n Equivalence in Joules: {convJoules(userValue)} \n Equivalence in tons of TNT: {convTNT(userValue)}")
