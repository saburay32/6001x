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
        elif guesword in secretWord and guesword in lettersGuessed :
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