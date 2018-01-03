'''
Created on Dec 28, 2017

@author: leahschwartz
'''
import random
def createDeck():
    #returns a list of all 52 cards with number and suit
    deck = []
    suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
    numbers = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    for number in numbers:
        for suit in suits:
            deck.append(number + " of " + suit)
    return deck
    
def getValue(card, hand):
    #card is string, hand is list, returns int value of card 
    number = card.split()[0]
    if number.isdigit():
        value = int(number)
    elif number != "Ace":
        value = 10
    return value

def getHandValue(hand):
    #hand is list, returns int value of whole hand
    handValue = 0
    aceCount = 0
    for card in hand:
        if card.split()[0] != "Ace":
            handValue += getValue(card, hand)
        else:
            aceCount += 1
    if aceCount > 0:     
        for num in range(aceCount):
            if handValue <= 10:
                handValue += 11
            else:
                handValue += 1
    return handValue
           
def dealCard(deck):
    #deck is list, returns string card, list deck with "dealt" card removed
    card = random.choice(deck)
    deck.remove(card)
    return card, deck

def dealHand(deck):
    #returns list of two random cards
    hand = [dealCard(deck)[0], dealCard(deck)[0]]
    return hand

def displayHand(hand):
    #prints cards and value of hand
    print ", ".join(hand)
    print "Value =", getHandValue(hand)
    
def endGame(playerHand,dealerHand):
    #prints winning and losing messages based on final hand values 
    keepGoing = raw_input("Press enter to continue") 
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)
    if dealerValue == 21 and playerValue <= 21:
        print "Dealer has blackjack! You lose."
    elif playerValue > 21:
        print "You busted! Game over."
    elif playerValue == 21:
        print "Congratulations, you have blackjack. You win!"
    elif dealerValue > 21:
        print "The dealer busted. You win!"
    elif playerValue > dealerValue:
        print "You beat the dealer! You win!"
    else:
        print "You lose. Better luck next time!"
                
                
def playGame(deck):
    #controls game play
    playerHand = dealHand(deck)
    dealerHand = dealHand(deck)
    print "Your Hand:"
    displayHand(playerHand)
    print "Dealer's Hand:"
    print dealerHand[0]+", unknown card"
    print "Value =", getHandValue([dealerHand[0]]),"+ ?"
    print "---------------------------------------"
    next = raw_input("Press enter to continue").lower()
    if getHandValue(playerHand) == 21:
        print "Congratulations! You have Blackjack!"
    else:
        hit = raw_input("Do you want another card? (Type hit me or stand)").lower()
        print "---------------------------------------"
        while hit == "hit me":
            playerHand.append(dealCard(deck)[0])
            handValue = getHandValue(playerHand)
            print "Your Hand:"
            displayHand(playerHand)
            print "Dealer's Hand:"
            print dealerHand[0]+", unknown card"
            print "Value =", getHandValue([dealerHand[0]]),"+ ?"
            if handValue < 21:
                hit = raw_input("Do you want another card? (Type hit me or stand)").lower()
                print "---------------------------------------"
            else:
                break
    if getHandValue(playerHand) >= 21:
        endGame(playerHand, dealerHand)
    else:
        reveal = raw_input("Press enter to reveal the dealer's hand")
        print "---------------------------------------"
        print "Your Hand:"
        displayHand(playerHand)
        print "Dealer's Hand:"
        displayHand(dealerHand)
        dealerValue = getHandValue(dealerHand)
        if dealerValue == 21:
            print "The dealer has blackjack! You lose."
        elif dealerValue >= 17:
            endGame(playerHand, dealerHand)
        elif dealerValue <= 16:
            keepGoing = raw_input("Press enter to see the dealer's next card")
            print "---------------------------------------"
            while dealerValue <= 16:
                dealerHand.append(dealCard(deck)[0])
                dealerValue = getHandValue(dealerHand)
                print "Your Hand:"
                displayHand(playerHand)
                print "Dealer's Hand:"
                displayHand(dealerHand)
                if dealerValue <= 16:
                    keepGoing = raw_input("Press enter to see the dealer's next card")
                    print "---------------------------------------"
                else:
                    break 
            endGame(playerHand, dealerHand)
        
                

if __name__ == '__main__':
    deck = createDeck()
    print "Ready to play Blackjack?"
    ready = raw_input("Type yes to play:").lower()
    if ready == "yes":
        playGame(deck)
        
    
   
    