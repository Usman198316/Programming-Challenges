def slayer():   
    slayer = str(input("Guess a 6 digit number SLAYER so that SLAYER + SLAYER + SLAYER = LAYERS \n Enter your guess for SLAYER >> "))
    layers = getLayers(slayer)
    checkGuess(slayer, layers)   
    
def getLayers(slayer):
    layers = str(slayer[1:6] + slayer[0])
    return layers
    
def checkGuess(slayer, layers):
    if int(slayer)*3 == int(layers):
        print(f" Your guess is correct : \n SLAYER + SLAYER + SLAYER = {int(slayer)*3} \n LAYERS = {layers} \n Thanks for playing.")
    else:
        print(f" Your guess is incorrect : \n SLAYER + SLAYER + SLAYER = {int(slayer)*3} \n LAYERS = {layers} \n Thanks for playing.")
                             
slayer()
