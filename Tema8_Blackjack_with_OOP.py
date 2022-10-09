# Tema08 - We`ll try and implement the game of Blackjack (also known as 21 in Ro:) using OOP strategies.
# The present notebook has different levels of suggestions depending on how hard you want to challenge yourself.
# Level 0 is the problem definition, while Level 1 and ongoing are a blueprint for how to implement it.

# Level 0:

# computer dealer - human player
# player - has a bankroll - places a bet and gets 2 cards
# dealer - places 1 card face up & 1 card face down
# dealer hits until reaches a score of at least 17
# player goal is to get closer to 21 than dealer
# actions: 1. hit (get another card); 2. stay (no more cards)
# when player stops:
# A) busts and loses
# B) dealer hits until: a) beats player b) busts
# face cards (J,Q,K) count as a value of 10
# Aces (A) count as either 1 or 11 whichever is preferable
# 2 Aces (A) = 21 not 22

# Level 1: Blueprint for the program, with the classes needed
# define yourself a suits tuple containig the possible suits (Hearts, Clubs...)
# a ranks tuple with all the possible ranks (2, 3 .... K, A)
# and a rank_to_value structure

#class Card:
# Should be a representation of some sort of a card.
#Should be able to understand the rank (2,3,.....K,A), suit (Diamonds, Hearts, Clubs, Spades) and probably the value of points as an integer.
#!Tip: use some globals to define all of the possible ranks, suits and associated value for the ranks
    #pass
#class Deck:
#Should create a new deck of 52 cards whenever we instantiate a deck.
#Should hold a list of the cards, be able to shuffle the order of the cards and also be able to deal a card.
#pass

#class Player:
#Should hold a Player`s current list of cards. A player should be able to add (when hitting) or remove cards (when restarting game)
#When adding cards, it should be either one (hit) card or two cards (when dealing at start of game).
# Player should be also able to bet an amount of chips from their bankroll at the begining of a round
    #pass

#class Dealer:
#Dealer is similar to Player with the exception that from the first 2 cards one is shown face up and the other face down.
    #pass

#def play_game():
#!Tip: Game will run in a while loop...
    #pass

# Level 2: this is the mappings structures that you could use for setting suits and ranks and mapping of values

# define yourself a suits tuple containig the possible suits (Hearts, Clubs...)
# a ranks tuple with all the possible ranks (2, 3 .... K, A)
# and a rank_to_value structure
#suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
#ranks = ('2', '3', '4', '5', '6', '7', '8',
#         '9', '10', 'J', 'Q', 'K', 'A')
#rank_to_value = {
#    '2': 2,
#    '3': 3,
#   '4': 4,
#    '5': 5,
#   '6': 6,
#    '7': 7,
#   '8': 8,
#    '9': 9,
#    '10': 10,
#    'J': 10,
#    'Q': 10,
#    'K': 10,
#    'A': 11
#}
# Level 3: this is the main loop of the game
#def game_on():
    # initialize player and dealer

    #while True:

# initialize deck and players hands
# check if player has any chips to play a round and ask for a bet
# deal cards
# handle player turn
# handle dealer turn
# handle win cases
# ask to play again

import random

suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
rank_to_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

playing = True


class Card:
# creeaza toate cartile
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
# creeaza pachetul de carti
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_combination = ''
        for card in self.deck:
            deck_combination += '\n ' + card.__str__()
        return 'The deck has: ' + deck_combination
# amesteca cartile
    def shuffle(self):
        random.shuffle(self.deck)
# alege o carte din pachet
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Player:
# arata toate cartile pe care le are jucatorul
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.total = 100
        self.bet = 0
# alege carte pentru jucator
    def add_card(self, card):
        self.cards.append(card)
        self.value += rank_to_value[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
# colecteaza castigul
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


class Dealer:

    def __init__(self):
        self.total = 100
        self.bet = 0
        self.cards = []
        self.value = 0
        self.aces = 0
# alege carte pentru dealer
    def add_card(self, card):
        self.cards.append(card)
        self.value += rank_to_value[card.rank]
        if card.rank == 'A':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Invalid number: ")
        else:
            if chips.bet > chips.total:
                print("You cannot bet more than 100 chips!")
            else:
                break

# alege carte cand introduce hit
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stay(deck, hand):
    global playing

    while True:
        ask = input("\nWould you like to hit or stay? Enter 'h' for hit or 's' for stay: ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Please try again!")
            continue
        break

# arata cartile la inceputul jocului, pentru jucator si dealer
def show_some(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>") # carte ascunsa pentru dealer
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

# arata cartile la sfarsitul jocului
def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# sfarsitul jocului

def player_busts(player, dealer, chips):
    print("PLAYER BUSTS!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("DEALER BUSTS!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()


def push(player, dealer):
    print("Its a push! Player and Dealer tie!")


# jocul

while True:
    print("Welcome to BlackJack!")

    # amesteca cartile
    deck = Deck()
    deck.shuffle()

    player_hand = Player()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Player()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # chips
    player_chips = Dealer()

    # pariul
    take_bet(player_chips)

    # arata cartile
    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stay(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("\nPlayer's winnings stand at", player_chips.total)

    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThank you for playing!")
        break