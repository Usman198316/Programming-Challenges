print("We are going to play a game. I want you to pick a number then do a series of calculations. I bet I know what the result of those calculations will be!")
answer = int(input("*You* This will be the answer. Select a number between 10-49 >> "))
factor =  99 - answer
num = int(input("*Player* Pick any number 50-99 >> "))
addedAns = num + factor
if addedAns > 100:
    addedAns -= 100
    addedAns += 1

result = num - addedAns
print(f"I said the answer was {answer} and the calculation result is {result}")
