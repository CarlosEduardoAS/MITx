# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:04:32 2021

@author: caear
"""
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False
    

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    str1 = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            str1 += letter
        else:
            str1 += ' _ '
    return str1


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    available = ''
    for letter in alphabet:
        if letter in lettersGuessed:
            available = available
        else:
            available += letter
    return available


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
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ', len(secretWord), ' letters long.')
    mistakesMade = 0
    lettersGuessed = []
    wrongletters = []
    while isWordGuessed(secretWord, lettersGuessed) == False and mistakesMade < 8:
        print('------------')
        print('You have ', (8-mistakesMade),' guesses left.')
        print('Available letters: ', getAvailableLetters(lettersGuessed+wrongletters))
        guess = str(input('Please guess a letter: ')).lower().strip()
        if guess in lettersGuessed or guess in wrongletters:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
        else:
            wrongletters.append(guess)
            print('Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ', secretWord, '.')

                
hangman('c')