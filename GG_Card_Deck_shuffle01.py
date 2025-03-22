# Card Deck Shuffle - This Program shuffles a deck of cards and distributes within 4 players

def Card_Deck():

    import random
    All_deck=[]
    
    deck_Hearts = ('HA','H2','H3','H4','H5','H6','H7','H8','H9','H10','HJ','HQ','HK')
    deck_Spades = ('SA','S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK')
    deck_Clubs = ('CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK')
    deck_Diamonds = ('DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK')

    All_deck = list(deck_Hearts + deck_Spades + deck_Clubs + deck_Diamonds)
    Shuffled_deck=[]

    for _ in range(52):  
        choice = random.choice(All_deck)  # Pick a random element  
        Shuffled_deck.append(choice)  
        All_deck.remove(choice)  # Remove chosen element to prevent repetition  

    print(Shuffled_deck)
    
    return Shuffled_deck

def main():
    import os
    import random
    
    # Clearing the Screen
    os.system('cls')

    my_Deck = Card_Deck()

   # print (my_Deck)

    player1_Deck = my_Deck[:13]
    player2_Deck = my_Deck[13:26]
    player3_Deck = my_Deck[26:39]
    player4_Deck = my_Deck[39:52]

    print ('Player 1 Deck : ',player1_Deck)
    print ('Player 2 Deck : ',player2_Deck)
    print ('Player 3 Deck : ',player3_Deck)
    print ('Player 4 Deck : ',player4_Deck)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()