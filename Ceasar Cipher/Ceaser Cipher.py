def ReturnEncryptedString():
    code = input("Enter in the code you would like to encrypt")
    code = code.upper()
    newString = ""
    tempArr = list(code)
    for oldChar in tempArr:
        newString += EncryptKey(oldChar)
    print(newString)
def ReturnDecryptedString():
    code = input("Enter in the code you would like to decipher")
    code = code.upper()
    newString = ""
    tempArr = list(code)
    for oldChar in tempArr:
        newString += DecodeKey(oldChar)
    print(newString)
def DecodeKey(char):
    #Create temp array for word
    #take i element in word array and shift it the ascii number back 5 letters
    asciiInt = ord(char)
    tempInt = ord(char)
    tempInt += 13
    #If ascii value is greater than 90 shift the original ascii value back by 26
    if(char == "!"):
        return char
    elif(char == " "):
        return char
    elif(tempInt > 90 ):
        asciiInt -=13
    else:
        asciiInt += 13
    #convert the ascii value to a character using the function chr()
    char = chr(asciiInt)
    #Append character to a new string
    return char
def EncryptKey(char):
    asciiInt = ord(char)
    tempInt = ord(char)
    tempInt -= 13
    if(char == "!"):
        return char
    elif(char == " "):
        return char
    elif(tempInt < 64 ):
        asciiInt +=13
    else:
        asciiInt -= 13
    #convert the ascii value to a character using the function chr()
    char = chr(asciiInt)
    #Append character to a new string
    return char
def PromptUser():
    answer = input("Do you want to decode or encrypt your message?")
    answer = answer.lower()
    if(answer == "encrypt"):
        ReturnEncryptedString()
    if(answer == "decode"):
        ReturnDecryptedString()

print("This is Ceaser's Cipher")
PromptUser()




#TODO Convert letter from alphabet 13 spaces or 13 spaces up in Ascii table

#Take user's input

#Convert
