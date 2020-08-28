import datetime
check = True
while check == True:
    start = datetime.datetime.now()
    correctWords = 0
    incorrectWords = 0
    print(" S P E L L   C H E C K E R\n\n   1. Check a file\n   2. Check a sentence\n\n   0. Quit\n")
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
        ignoredNum = 0
        addedNum = 0
        markedNum = 0
        realWords = dictionary.readlines()
        #Checks if each word is in the list realWords
        for word in range(len(splitWords) - 1):
            if len(splitWords[word]) < 1:
                splitWords.remove(splitWords[word])
            if (splitWords[word] + "\n").casefold() in realWords:
                correctWords += 1
            else:
                print(splitWords[word] + " not found\n")
                print("1. Ignore the word.")
                print("2. Mark the word as incorrect")
                print("3. Add word to dictionary\n")
                valid = False
                while valid == False:
                    #Validate choice
                    catagorise = 0
                    try:
                        catagorise = int(input("Enter choice: "))
                    except:
                        print("That is not a valid choice please choose 1, 2 or 3")
                        continue;
                    if (catagorise <= 3 and catagorise >= 1):
                        valid = True
                    else:
                        print("That is not a valid choice please choose 1, 2 or 3")
                    #Execute choice
                    if catagorise == 1:
                        #Ignore the word
                        splitWords[word] = ("!" + splitWords[word] + "!")
                        ignoredNum += 1
                    if catagorise == 2:
                        #Mark as incorrect
                        splitWords[word] = ("?" + splitWords[word] + "?")
                        markedNum += 1
                    if catagorise == 3:
                        #Add to dictionary
                        with open("EnglishWords.txt", "a") as dictionary:
                            dictionary.write("\n" + splitWords[word] + "\n")
                        splitWords[word] = ("*" + splitWords[word] + "*")
                        addedNum += 1
                incorrectWords += 1
    with open("CorrectedWords.txt", "w") as correctedWords:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M")
        correctedWords.write(now + "\n")
        correctedWords.write("Number of words: " + str(correctWords + incorrectWords) + "\n")
        correctedWords.write("Number of correctly spelt words: " + str(correctWords) + "\n")
        correctedWords.write("Number of incorrectly spelt words: " + str(incorrectWords) + "\n")
        correctedWords.write("  Number ignored: " + str(ignoredNum) + "\n")
        correctedWords.write("  Number added to dictionary: " + str(addedNum) + "\n")
        correctedWords.write("  Number marked: " + str(markedNum) + "\n")
        for word in splitWords:
            correctedWords.write(word + " ")
    #Prints data for user
    end = datetime.datetime.now()
    elapsed = end - start
    print("Number of words: " + str(correctWords + incorrectWords))
    print("Number of correctly spelt words: " + str(correctWords))
    print("Number of incorrectly spelt words: " + str(incorrectWords))
    print("  Number ignored: " + str(ignoredNum))
    print("  Number added to dictionary: " + str(addedNum))
    print("  Number marked: " + str(markedNum) + "\n")

    print("Time elapsed (Hours:Minutes:Seconds): " +str(elapsed) + "\n")
    #Checks if user wants to check another sentence
    again = input("Press q [enter] to quit or any other key [enter] to go again: ")
    if again == "q":
        check = False
    else:
        check = True
