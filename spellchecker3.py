import datetime
check = True
while check == True:
    start = datetime.datetime.now()
    correctWords = 0
    incorrectWords = 0
    print(" S P E L L   C H E C K E R\n\n   1. Check a file\n   2. Check a sentence\n\n   0. Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        #Choose a file to be checked
        chosenFile = input("Enter the name of the file to spellcheck: ")
        with open(chosenFile, "r") as words:
            words = words.read()
            words = words.casefold()
    elif choice == "2":
        #Takes users input sentence
        words = input("Please enter a sentence: ")
        words = words.casefold()
    elif choice == "0":
        #Quits
        break;
    else:
        print("\n--- NOT A VALID RESPONSE, PLEASE ENTER A VALUE FROM 0-2 ---\n")
        continue;

    #Removes all non 'a-z' or 'A-Z' charecters except spaces
    for letter in words:
        if (ord(letter) < 97 or ord(letter) > 122) and (ord(letter) != 32):
            words = words.replace(letter, "")
    splitWords = words.split(" ", -1)
    #Import each line of EnglishWords.txt into a list realWords
    with open("EnglishWords.txt", "r") as dictionary:
        realWords = dictionary.readlines()
        #Checks if each word is in the list realWords
        for word in range(len(splitWords) - 1):
            if len(splitWords[word]) < 1:
                splitWords.remove(splitWords[word])
                print(splitWords)
            if (splitWords[word] + "\n").casefold() in realWords:
                correctWords += 1
            else:
                incorrectWords += 1
                splitWords[word] = ("?" + splitWords[word] + "?")
    with open("CorrectedWords.txt", "w") as correctedWords:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M")
        correctedWords.write(now + "\n")
        correctedWords.write("Number of words: " + str(correctWords + incorrectWords) + "\n")
        correctedWords.write("Number of correctly spelt words: " + str(correctWords) + "\n")
        correctedWords.write("Number of incorrectly spelt words: " + str(incorrectWords) + "\n")
        for word in splitWords:
            correctedWords.write(word + " ")
    #Prints data for user
    end = datetime.datetime.now()
    elapsed = end - start
    print("Time elapsed (Hours:Minutes:Seconds): " +str(elapsed))
    print("Number of words: " + str(correctWords + incorrectWords))
    print("Number of correctly spelt words: " + str(correctWords))
    print("Number of incorrectly spelt words: " + str(incorrectWords))
    #Checks if user wants to check another sentence
    again = input("Press q [enter] to quit or any other key [enter] to go again: ")
    if again == "q":
        check = False
    else:
        check = True
