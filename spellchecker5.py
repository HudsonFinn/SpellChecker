import datetime
import os.path
from difflib import SequenceMatcher

check = True
while check == True:
    start = datetime.datetime.now()
    correctWords = 0
    incorrectWords = 0
    print("┏"+ "━" * 20)
    print("┃ S P E L L   C H E C K E R\n┃\n┃   1. Check a file\n┃   2. Check a sentence\n┃\n┃   0. Quit\n┃")
    choice = str(input(u"\u2517━━━Enter choice: "))
    if choice == "1":
        #Choose a file to be checked
        fileChosen = False
        while fileChosen == False:
            print("\n\n┏"+ "━" * 20)
            print("┃ L O A D  F I L E\n┃\n┃   Enter a file name\n┃   then press [enter]\n┃\n┃")
            chosenFile = input(u"\u2517━━━Filename: ")
            if os.path.exists(chosenFile) == True:
                with open(chosenFile, "r") as words:
                    words = words.read()
                    words = words.casefold()
                fileChosen = True
            else:
                print("\n ━━━ File not found please ensure file is in directory ━━━")
                continue
    elif choice == "2":
        #Takes users input sentence
        print("\n\n┏"+ "━" * 20)
        print("\n\n┃ E N T E R  S E N T E N C E\n┃\n┃   Enter a sentence\n┃   then press [enter]\n┃\n┃")
        words = input(u"\u2517━━━Sentence: ")
        words = words.casefold()
    elif choice == "0":
        #Quits
        break;
    else:
        print("\n━━━ NOT A VALID RESPONSE, PLEASE ENTER A VALUE FROM 0-2 ━━━\n")
        continue;

    #Removes all non 'a-z' charecters except spaces
    for letter in words:
        if (ord(letter) < 97 or ord(letter) > 122) and (ord(letter) != 32):
            words = words.replace(letter, "")
    splitWords = words.split(" ", -1)
    #Import each line of EnglishWords.txt into a list realWords
    with open("EnglishWords.txt", "r") as dictionary:
        ignoredNum = 0
        addedNum = 0
        markedNum = 0
        correctedNum = 0
        realWords = dictionary.readlines()
        #Gives options on what the user can do with incorrect words
        for word in range(len(splitWords) - 1):
            #Removes any "words" in the list that have no letters
            if len(splitWords[word]) < 1:
                splitWords.remove(splitWords[word])
            #Checks if word is in the list of real words
            if (splitWords[word] + "\n").casefold() in realWords:
                correctWords += 1
            #If not presents options for user
            else:
                #Calculates the most probable correct word
                incorrectWords += 1
                probabilityOld = 0.0
                autoCorrectChoice = ""
                for realWord in realWords:
                    probabilityNew = SequenceMatcher(None, splitWords[word], realWord).ratio()
                    if probabilityNew > probabilityOld:
                        autoCorrect = realWord
                        probabilityOld = probabilityNew
                #Presents autocorrect choice
                while ((autoCorrectChoice.casefold() != "y") and (autoCorrectChoice.casefold() != "n")):
                    print("\n\n┏"+ "━" * 20)
                    print("┃ W O R D  N O T  F O U N D\n┃\n┃   " + splitWords[word] + "\n┃\n┃   did you mean\n┃\n┃   " + autoCorrect + "┃")
                    autoCorrectChoice = str(input(u"\u2517━━━Enter [y] or [n]: "))
                #Replaces word if user selects yes to autocorrect
                if autoCorrectChoice.casefold() == "y":
                    splitWords[word] = autoCorrect[0:-1]
                    correctedNum += 1
                    continue
                #Presents other options if users selects no to autocorrect
                print("\n\n┏"+ "━" * 20)
                print("┃ W O R D  N O T  F O U N D\n┃\n┃   " + splitWords[word] + "\n┃")
                print("┃ 1. Ignore the word.")
                print("┃ 2. Mark the word as incorrect")
                print("┃ 3. Add word to dictionary\n┃")
                valid = False
                while valid == False:
                    #Validate choice
                    catagorise = 0
                    try:
                        catagorise = int(input(u"\u2517━━━Enter choice: "))
                    except:
                        print("That is not a valid choice please choose 1, 2 or 3")
                        continue;
                    #Execute choice
                    if catagorise == 1:
                        #Ignore the word
                        valid = True
                        splitWords[word] = ("!" + splitWords[word] + "!")
                        ignoredNum += 1
                    elif catagorise == 2:
                        #Mark as incorrect
                        valid = True
                        splitWords[word] = ("?" + splitWords[word] + "?")
                        markedNum += 1
                    elif catagorise == 3:
                        #Add to dictionary
                        valid = True
                        with open("EnglishWords.txt", "a") as dictionary:
                            dictionary.write("\n" + splitWords[word] + "\n")
                        splitWords[word] = ("*" + splitWords[word] + "*")
                        addedNum += 1
                    else:
                        print("That is not a valid choice please choose 1, 2 or 3")
                        print("Broke")
    #Creats or overwrites file to fill with stats and words with punctuation !!??** annotation
    with open("CorrectedWords.txt", "w") as correctedWords:
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M")
        correctedWords.write(now + "\n")#
        correctedWords.write("Number of words: " + str(correctWords + incorrectWords) + "\n")
        correctedWords.write("Number of correctly spelt words: " + str(correctWords) + "\n")
        correctedWords.write("Number of incorrectly spelt words: " + str(incorrectWords) + "\n")
        correctedWords.write("  Number ignored: " + str(ignoredNum) + "\n")
        correctedWords.write("  Number added to dictionary: " + str(addedNum) + "\n")
        correctedWords.write("  Number marked: " + str(markedNum) + "\n")
        for word in splitWords:
            correctedWords.write(word + " ")
            print(word)
    #Prints data for user in console
    end = datetime.datetime.now()
    elapsed = end - start
    print("\n\n┏"+ "━" * 20)
    print("┃ R E S U L T S\n┃\n┃   ")
    print("┃Number of words: " + str(correctWords + incorrectWords))
    print("┃Number of correctly spelt words: " + str(correctWords))
    print("┃Number of incorrectly spelt words: " + str(incorrectWords))
    print("┃  Number ignored: " + str(ignoredNum))
    print("┃  Number added to dictionary: " + str(addedNum))
    print("┃  Number marked: " + str(markedNum))
    print("┃  Number changed: " + str(correctedNum) + "\n┃")

    print("┃Time elapsed (Hours:Minutes:Seconds): " +str(elapsed))
    print(u"\u2517" + "━" * 20)
    #Checks if user wants to check another sentence
    again = input("Press q [enter] to quit or any other key [enter] to go again: ")
    if again == "q":
        check = False
    else:
        check = True
