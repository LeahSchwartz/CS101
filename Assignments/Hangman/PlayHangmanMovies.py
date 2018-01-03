'''
Created on Oct 20, 2017
@author: Leah Schwartz
ls323
'''

import random

def fileToStringList(filename):
    """
    filename is a file, 
    returns a list of strings, each string represents
    one line from filename
    """
    #reads in file and returns list of strings
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist
    
     
def getPossibleWords(wordlist,length):
    """
    returns a list of words from wordlist having a 
    specified length 
    """
    wordlist = [w for w in wordlist if len(w.split()) == length]
    # TODO - write a list comprehension to return 
    # only those words of the specified length
    return wordlist

def displayGuess(wordList):
    '''
    wordList is a list of characters with letters correctly
    guessed and '_' for letters not quessed yet
    returns the list as a String
    '''
    return ' '.join(wordList)

def guessStart(word):
    '''
    returns a list of single characters '_' the
    same size as word
    '''
    startingTitle = []
    for ch in word:
        if ch.isalpha():
            startingTitle.append("_")
        else:
            startingTitle.append(ch)  
    return startingTitle

def updateLetter(guessList,wordToGuess,letter):
    '''
    wordToGuess is the word the user is trying to guess.
    guessList is the word to guess as a list of characters, but
    only including the letters the user has guessed and showing
    the character '_' if a letter hasn't been guessed yet.
    letter is the current letter the user has guessed. 
    
    Modify guessList to include letter in its proper locations if 
    letter is in wordToGuess.
    
    For example, if the wordToGuess is "baloney" and so far only a and
    e have been guessed, then guessList is ['_','a','_','_','_','e','_']
    If letter is 'o', then guessList is modified to now be:
    ['_','a','_','o','_','e','_']
    
    '''
    #replaces blank with letter if guessed right and tells if guess is correct
    for i in range(len(wordToGuess)):
        if wordToGuess[i].lower() == letter.lower():
            guessList[i] = wordToGuess[i] 
    if letter.lower() in wordToGuess or letter.upper() in wordToGuess:
        print "You guessed a letter" 
    else:
        print "That's a miss"  

def countIncompleteWords(guessList): 
    #counts how many words are not complete based on if there is a blank
    incompleteWords = 0
    joinGuessList = "".join(guessList)
    splitGuessList = joinGuessList.split()
    for word in splitGuessList:
        if "_" in word:
            incompleteWords += 1
    return incompleteWords #returns int
                          
def playGame(words):
    '''
    Play the game. Let the user know if they won or not.
    '''
    #setup for game

    guessLength = ((raw_input("how many words in title to guess? "))) #input how long a title they want
    while True:
        if not str(guessLength).isdigit() or int(guessLength) < 1: #makes sure input is a number 1 or more 
            print "Please enter a number that is 1 or more"
            guessLength = ((raw_input("how many words in title to guess? ")))
        if str(guessLength).isdigit() and int(guessLength) >= 1: #lets game continue as long as input is number 1 or more 
            guessLength = int(guessLength) #turns input into number
            break
    missesAllowed = (raw_input("how many misses are you allowed? ")) #input misses allowed
    while True: #makes sure input is a number
        if not missesAllowed.isdigit():
            print "Please enter a number"
            missesAllowed = (raw_input("how many misses are you allowed? "))
        else:
            missesAllowed = int(missesAllowed) #turns input into number
            break
        
    wordsOfLength = getPossibleWords(words,guessLength)    
    wordToGuess = random.choice(wordsOfLength)
    guessList = guessStart(wordToGuess)
    wordGuess = ""
    Misses = 0
    lettersNotGuessed = "abcdefghijklmnopqrstuvwxyz" #initial letter list
    
    # start the guessing
    while True:
        if guessList.count('_') == 0:
            # all letters guessed
            break
        print # output to print for each round
        print "Guessed so far:", displayGuess(guessList)
        letter = raw_input("Guess a letter or enter + to guess the movie title: ")
        while True: #makes sure user enters letter
            if not letter.isalpha() and letter != "+": 
                print "Please enter a letter or +"
                letter = raw_input("Guess a letter or enter + to guess the word: ")
            else:
                break
        if letter == "+":
            wordGuess = raw_input("Guess the movie title:") #lets them guess word
            if wordGuess.lower() == wordToGuess.lower(): #wrong or right if they guessed the word
                print "You win. You guessed the movie", wordToGuess 
                break
            else:
                print "You lost. The correct movie was", wordToGuess
                break
        else: #handles already guessed letters
            if (letter.lower() in guessList or letter.upper() in guessList) or letter.lower() not in lettersNotGuessed: #already guessed letter
                Misses += 1
                print "You already guessed that letter!"
                print "Letters not guessed are:", lettersNotGuessed
                print "Number of misses left are:", (missesAllowed - Misses)
                print "Words left to complete are:", countIncompleteWords(guessList)
            else:        
                updateLetter(guessList, wordToGuess, letter) #updates after guess if letter not yet guessed
                lettersNotGuessed = "".join([w for w in lettersNotGuessed if w != letter.lower()])
                print "Letters not guessed are:", lettersNotGuessed
                if letter.lower() not in wordToGuess.lower():
                    Misses += 1
                print "Number of misses left are:", (missesAllowed - Misses)
                print "Words left to complete are:", countIncompleteWords(guessList)
            if (missesAllowed - Misses) == 0: #ran out of misses
                print "You lost. You ran out of misses. The correct movie was", wordToGuess
                break   
    # game over
    if (missesAllowed - Misses) > 0 and wordGuess == "": #means that player still had misses and didn't try to guess word so they won
        print "You win. You guessed the movie", wordToGuess 
    print "You missed", Misses, "times"

    
if __name__ == '__main__':
    words = fileToStringList('movies.txt')
    print "Number of movies is:", len(words)
    playGame(words)