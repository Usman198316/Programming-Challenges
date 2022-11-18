def main():
    Option = menu()
    if Option == "1":
        Key = int(input("Please enter the key (number from 1 to 26) >> "))
        Message = str(input("Please enter the message you want to encrypt >> "))
        encryptedMessage = encrypt(Message, Key)
        print(f"Original Message : '{Message}' \nEncrypted Message : '{encryptedMessage}'")
    elif Option == "2":
        Key = int(input("Please enter the key (number from 1 to 26) >> "))
        Message = str(input("Please enter the message you want to decrypt >> "))
        decryptedMessage = decrypt(Message, Key)
        print(f"Original Message : '{Message}' \nDecrypted Message : '{decryptedMessage}'")
    elif Option == "3":
        Message = str(input("Please enter the encrypted message >> "))
        findKey(Message)
def menu():
    option = str(input("================ \n1. Encryption \n2. Decryption \n3. Key Finder \n================ \n>> "))
    return option

def encrypt(Message, Key):
    encryptedMessage = ""
    for char in Message:
        if char.isalpha():
            if (char.isupper() and (ord(char)+Key) > 90):
                newChar = chr((ord(char)+Key)-26)
            elif char.islower() and (ord(char)+Key) > 122:
                newChar = chr((ord(char)+Key)-26)
            else:
                newChar = chr(ord(char)+Key)
            encryptedMessage += newChar
        elif not char.isalpha():
            encryptedMessage += char
    return encryptedMessage

def decrypt(Message, Key):
    decryptedMessage = ""
    for char in Message:
        if char.isalpha():
            if char.isupper() and (ord(char)-Key) < 65:
                newChar = chr((ord(char)-Key)+26)
            elif char.islower() and (ord(char)-Key) < 97:
                newChar = chr((ord(char)-Key)+26)
            else:
                newChar = chr(ord(char)-Key)
            decryptedMessage += newChar
        elif not char.isalpha():
            decryptedMessage += char
    return decryptedMessage

def findKey(Message):
    for i in range(26):
        print(f"{i} {decrypt(Message, i)}")
    

        
##        if char != " ":
##            newChar = chr(ord(char) + Key)
##            encryptedMessage += newChar
##        elif char == " ":
##            encryptedMessage += " "
##    return encryptedMessage
        
    
main()
