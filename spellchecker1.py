words = input("Please enter a sentence: ") #Takes users input sentence
splitWords = words.split(" ", -1)
print(splitWords)
with open("EnglishWords.txt", "r") as dictionary:
    realWords = dictionary.readlines() #Import each line of EnglishWords.txt into a list realWords
    for word in range(len(splitWords)): #Loops through the sentence
        if (splitWords[word] + "\n") in realWords: #Adds a new line char and checks if the result is in the dict
            print(splitWords[word] + " spelt correctly")
        else:
            print(splitWords[word] + " not found in dictionary")
