# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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
    secretWord:  строка, слово, которое пользователь угадывает
    lettersGuessed:  список, какие буквы были угаданы до сих пор
    returns: boolean, True если все буквы секретного слова находятся в угаданных буквах;
      False otherwise
    '''
    for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: строка, слово, которое пользователь угадывает
    lettersGuessed: список, какие буквы были угаданы до сих пор,
    returns: строку, состоящую из букв и подчеркиваний, которая представляет
    какие буквы в секретном слове были угаданы до сих пор.
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
    lettersGuessed: перечислите, какие буквы были угаданы до сих пор
    returns: строка, состоящая из букв, не отгаданные.
    '''
    for i in lettersGuessed:
        if i in abc:
            abc = abc.replace(i, '')
    return abc

def hangman(secretWord):
    lettersGuessed = str()
    count = 8
    '''
    secretWord: строка, секретное слово, которое нужно угадать.

    lettersGuessed:  Буквы, которые были угаданы до сих пор.
    mistakesMade: Количество неверных предположений, сделанных до сих пор.
    availableLetters: Буквы, которые еще можно угадать.
     Каждый раз, когда игрок угадывает букву,
     угаданная буква должна быть удалена из доступных писем
    (и если они угадывают букву, которой нет в доступных письмах,
    вы должны напечатать сообщение о том,
    что они уже догадались об этом - так что попробуйте еще раз!).

    '''
    print("\nWelcome to the game, Hangman!\nI am thinking of a word that is "+str(len(secretWord))+" letters long.")
    print("___________")
    while isWordGuessed(secretWord, lettersGuessed) == False and count > 0:

        print('You have ' + str(count) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guesword = input('Please guess a letter:').lower()
        if guesword in secretWord and guesword not in lettersGuessed :
            lettersGuessed+=guesword
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("___________")
        elif guesword in  guesword in lettersGuessed :
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("___________")
        elif guesword not in secretWord :
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed += guesword
            print("___________")
            count -= 1
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + '.')









# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print('Secert Word: ',secretWord)
hangman(secretWord)
