import random

file = open("gburg.txt","r")

def scrambleWord(word):


    #Split word
    wordArr = list(word)
    #Get first letter Using a first letter index
    firstLetter = wordArr[0]
    #Get last letter using a last letter index
    lastLetterIndex = len(wordArr)-1
        #If Last letter is a punctuation get the prevoius latter
    if wordArr[lastLetterIndex] == "'" or wordArr[lastLetterIndex] == "," or wordArr[lastLetterIndex] == "-" or wordArr[lastLetterIndex] == ".":
            #Decrease last letter index by 1
        lastLetterIndex -= 1

    #Create a middle section string using slice
    middleSection = word[1:lastLetterIndex]
    #Make the middle section into an array
    middleSectionArr = list(middleSection)
    #Shuffle the middle section array
    random.shuffle(middleSectionArr)
    #Concantenate the first letter the middle section string and the last letter
    finalString = firstLetter[0] + "".join(middleSectionArr)+ wordArr[lastLetterIndex]
    #If the last character of the array is punctuation Concantenate the stiring
    if wordArr[len(wordArr)-1] == "," or wordArr[len(wordArr)-1] == "." or wordArr[len(wordArr)-1] == "-":
    #Return the final stirng
        finalString = finalString + wordArr[len(wordArr)-1]
    return finalString

    #Scramble the word



#Go through every line of the file

for line in file:
    for word in line.split():
        if len(word) > 3:
            print(scrambleWord(word))
        else:
             print(word)

file.close()





#feed each word into scrambeld word

