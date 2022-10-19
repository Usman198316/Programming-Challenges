def stringVowels(string):
    vowelList = []
    for char in string:
        if char in "AEIOU":
            vowelList.append(char)

    return vowelList

def stringConsonants(string):
    consonantList = []
    for char in string:
        if char in "BCDFGHJKLMNPQRSTVXZWY":
            consonantList.append(char)

    
        
   
    

def stuart_score(string, consonantList):
    print("")
    
    
        
            

  

def string():
    
    string = str(input("Enter the string >> "))
    try:
        if string.isalpha() == True:
            string = string.upper()
        else:
            raise Exception
    except:
        print("Enter a valid string please")

    stringConsonants(string)







string()
        


