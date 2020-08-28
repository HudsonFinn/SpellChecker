check = True
while check == True:
    correctWords = 0
    incorrectWords = 0
    #Takes users input sentence and splits it into a list
    words = input("Please enter a sentence to spellcheck: ")
    words = words.casefold()
    #Removes all non 'a-z' or 'A-Z' charecters
    i = 0
    for letter in words:
        if ((ord(letter) > 90 or ord(letter) < 65) and ((ord(letter) < 97 or ord(letter) > 122))) and (ord(letter) != 32):
            words = words.replace(letter, "")
    splitWords = words.split(" ", -1)
    #Import each line of EnglishWords.txt into a list realWords
    with open("EnglishWords.txt", "r") as dictionary:
        realWords = dictionary.readlines()
        #Checks if each word is in the list realWords
        for word in range(len(splitWords)):
            if len(splitWords[word]) < 1:
                splitWords.remove(splitWords[word])
            if (splitWords[word] + "\n") in realWords:
                print(splitWords[word] + " spelt correctly")
                correctWords += 1
            else:
                print(splitWords[word] + " not found in dictionary")
                incorrectWords += 1
    #Prints data for user
    print("Number of words: " + str(correctWords + incorrectWords))
    print("Number of correctly spelt words: " + str(correctWords))
    print("Number of incorrectly spelt words: " + str(incorrectWords))
    #Checks if user wants to check another sentence
    again = input("Press q [enter] to quit or any other key [enter] to go again: ")
    if again == "q":
        check = False
    else:
        check = True
