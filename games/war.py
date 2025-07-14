# It is a card game
import random # To select the random values from the card deck


values = {
        "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven":7,
        "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14
    }
black_jack_values =  {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
suits = ("Hearts", "Clubs", "Spades", "Diamonds") # Taking tuple because we dont want to update this. 
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace") # Tuple because dont want to change/update values

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = black_jack_values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

class Deck:

    def __init__(self):
        self.all_cards = []

        # Create a fresh card deck of 52 cards
        for suit in suits:
            for rank in ranks:
                # Create the card object
                self.all_cards.append(Card(suit, rank))

    def __str__(self):
        return f"Deck of card {self.all_cards}"
    
    def shuffle_cards(self):
        """
        Shuffle the card and give random order of the card
        """
        random.shuffle(self.all_cards) # it returns None

    def deal_one(self):
        """
        It will remove the card from the deck as a deal and update the deck count from 52
        """
        return self.all_cards.pop()
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # Check for list type
        if type(new_cards) == type([]):
            # list of multiple card object
            self.all_cards.extend(new_cards)
        else:
            # sigle card object
            self.all_cards.append(new_cards)




if __name__ == "__main__":
    # Game setup
    #   create 2 players
    player_one = Player("Player ONE")
    player_two = Player("Player TWO")
    print(f"{player_one}, {player_two}")
    # Create a fresh Deck
    new_deck = Deck()
    new_deck.shuffle_cards()

    # Split the cards between 2 players
    for card_index in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    
    # Check for Game ON
    game_on = True
    # set counter to count the game
    counter = 0

    while game_on:
        counter += 1
        print(f"Rounf {counter}")
        # Check condtion is both the player have card/are they out of cards
        if len(player_one.all_cards) == 0:
            print(f"{player_one.name} is out of cards. {player_two.name} winds the war!")
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print(f"{player_two.name} is out of cards. {player_one.name} winds the war!")
            game_on = False
            break
        


        # Start the new Round
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        print(player_one_cards[0], player_two_cards[0])

        # while at_war 
        # If both player draw same card
        at_war = True
        # if player_one_cards[0] == player_two_cards[0]:
        #     at_war = True
        while at_war:
            # Draw a set of cards from the deck
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print("You are at WAR!!")
                if len(player_one.all_cards) < 3:
                    print(f"{player_one.name} not able to play the WAR.")
                    print(f"{player_two.name} wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print(f"{player_two.name} not able to play the WAR.")
                    print(f"{player_one.name} wins!")
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
