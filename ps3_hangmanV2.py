import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    for x in secretWord:
        if x in lettersGuessed:
            string += x
        else:
            string += '_'
    return string

def getAvailableLetters(lettersGuessed):
    abc = str('abcdefghijklmnopqrstuvwxyz')
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for i in lettersGuessed:
        if i in abc:
            abc = abc.replace(i, '')
    return abc
# def getAvailableLetters(lettersGuessed):
#     '''
#     lettersGuessed: list, what letters have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#     notGuessed = []
#
#     for x in range(26):
#         notGuessed += chr(x + ord('a'))
#
#     for y in lettersGuessed:
#         notGuessed.remove(y)
#
#     string = ""
#     for z in notGuessed:
#         string += z
#
#     return string


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print(f"I am thinking of a word that is {len(str(secretWord)) }letters long.")
    print(secretWord)
    print("_________")
    lettersGuessed = []
    Guess = 8

    while not isWordGuessed(secretWord, lettersGuessed) and Guess > 0:
        print(f"You hav{len(str(Guess))} guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        while True:
            guessValue = input("Please guess a letter").lower()
            if guessValue in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print("_________")
                print("You have" + str(len(Guess)) + " guesses left.")
                print("Available letters: " + getAvailableLetters(lettersGuessed))
            else:
                break
        lettersGuessed += guessValue
        if isWordGuessed(secretWord, lettersGuessed):
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("_________")

            break
        elif guessValue in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("_________")
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            print("_________")
            Guess -= 1

        if Guess == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + '.')


secretWord = chooseWord(wordlist).lower
hangman(secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)