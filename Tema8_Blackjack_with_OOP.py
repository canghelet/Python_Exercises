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

culori = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
valori = ('2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A')
valori_in_joc = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

class Card:  # carte de joc
    """Should be a representation of some sort of a card.
    Should be able to understand the rank (2,3,.....K,A), suit (Diamonds, Hearts, Clubs, Spades) and probably the value of points as an integer.
    !Tip: use some globals to define all of the possible ranks, suits and associated value for the ranks"""

    def __init__(self, valoare, culoare):
        self.valoare = valoare
        self.culoare = culoare
        self.punctaj = valori_in_joc[valoare]

    def __str__(self):
        return f"{self.valoare} de {self.culoare}"


c1 = Card("A", "Inima rosie")
print(c1)
#A de inima rosie

from random import shuffle


class Deck:  # pachet de carti
    """Should create a new deck of 52 cards whenever we instantiate a deck.
    Should hold a list of the cards, be able to shuffle the order of the cards and also be able to deal a card."""

    def __init__(self):
        self.pachet_carti = []
        # ce inseamna tot pachetul de carti? cum il cream?
        for valoare in valori:
            for culoare in culori:
                carte = Card(valoare, culoare)
                self.pachet_carti.append(carte)

    # amestecam pachet
    def amestecare_pachet(self):
        shuffle(self.pachet_carti)

    # tragem carte
    def trage_carte(self):
        carte = self.pachet_carti.pop()
        return carte


lst = [1, 2, 3, 4]
lst.pop()  # returneaza si elimina ultimul elem din lista
pachet = Deck()
for c in pachet.pachet_carti:
    print(c)


class Player:
    """Should hold a Player`s current list of cards. A player should be able to add (when hitting) or remove cards (when restarting game)
    When adding cards, it should be either one (hit) card or two cards (when dealing at start of game).
    Player should be also able to bet an amount of chips from their bankroll at the begining of a round"""

    def __init__(self, nume, sold):
        self.nume = nume
        self.sold = sold
        self.carti = []
        self.scor = 0
        self.nr_asi = 0  # avem nevoie de un atribut care sa memoreze cati 'A' avem in mana pentru a putea modifica punctaj din 11 in 1 la nevoie

    def __str__(self):
        return f"{self.nume} are soldul = {self.sold}"

    def adauga_carte(self, carte_noua):
        print(f"{self.nume} a tras o carte")
        self.carti.append(carte_noua)
        self.scor += carte_noua.punctaj
        if carte_noua.valoare == 'A':
            self.nr_asi += 1
        if len(self.carti) == 2 and self.scor == 22:  # cazul in care avem 2 de 'A' in mana, scorul trebuie sa fie 21!
            self.scor = 21
        while self.scor > 21 and self.nr_asi:  # ajustam scorul in functie de cati Asi avem in mana daca s-a trecut de 21
            # de ex: ['A', 2] = 11 + 2 = 13  + carte_noua('K')  => 13 + 10 = 23 , dar avem 'A' in lista de carti => 23-10=13
            self.scor -= 10
            self.nr_asi -= 1

            # cand incepe o noua tura vrem sa ii golim mana (stergem cartile pe care le are)

    def golire_mana(self):
        self.carti.clear()
        self.scor = 0

    def arata_mana(self):
        print(f"{self.nume} are in mana: {[str(c) for c in self.carti]} cu scorul: {self.scor}")

    def verificare_sold(self):
        return self.sold > 0

    def pariaza(self):
        suma_pariata = int(input("Alege suma pariata: "))
        # tot cere input atata timp cat suma introdus e mai mare ca sold
        while self.sold < suma_pariata:
            print("Nu aveti destui bani!")
            suma_pariata = int(input("Alege suma pariata: "))

        self.sold -= suma_pariata
        return suma_pariata


class Dealer:
    """Dealer is similar to Player with the exception that from the first 2 cards one is shown face up and the other face down.
    """

    def __init__(self):
        self.nume = 'Dealer'
        self.carti = []
        self.scor = 0
        self.nr_asi = 0

    def verificare_sold(self):
        return self.sold > 0

    def adauga_carte(self, carte_noua):
        print(f"{self.nume} a tras o carte")
        self.carti.append(carte_noua)
        self.scor += carte_noua.punctaj
        if carte_noua.valoare == 'A':
            self.nr_asi += 1
        if len(self.carti) == 2 and self.scor == 22:  # cazul in care avem 2 de 'A' in mana, scorul trebuie sa fie 21!
            self.scor = 21
        while self.scor > 21 and self.nr_asi:  # de ex: ['A', 2] = 11 + 2 = 13  + carte_noua('K')  => 13 + 10 = 23 , dar avem 'A' in lista de carti => 23-10=13
            self.scor -= 10
            self.nr_asi -= 1

    def arata_mana(self,
                   arata_o_carte=False):  # in prima faza a jocului, Dealer`ul arata doar o carte, cealalta o pastreaza ascunsa pana termina de jucat Player`ul
        if arata_o_carte:
            print(f"{self.nume} are in mana: {self.carti[0]} cu scorul: {self.carti[0].punctaj}")
        else:
            print(f"{self.nume} are in mana: {[str(c) for c in self.carti]} cu scorul: {self.scor}")

    def golire_mana(self):
        self.carti.clear()
        self.scor = 0
    # dealer e similar cu player, doar ca nu pariaza

    # regula cu trasul cartilor pana ajunge la 17 se implementeaza in play_game


def play_game():
    """!Tip: Game will run in a while loop..."""
    # initialize player and dealer
    dealer = Dealer()

    nume_jucator = input("Introduceti numele jucatorului: ")
    sold = int(input("Alegeti suma de bani de pariat: "))
    player = Player(nume_jucator, sold)

    while True:
        # initialize deck and players hands (initializare pachet si mainile jucatorilor)
        pachet = Deck()
        pachet.amestecare_pachet()
        dealer.golire_mana()
        player.golire_mana()

        print(player)

        # check if player has any chips to play a round and ask for a bet (verificare sold jucator si interogare pariu)
        if not player.verificare_sold():
            print(f"{player.nume} nu mai are bani :(... Multumim de bani!")
            break

        pariu = player.pariaza()

        # deal cards
        # 1.playerul primeste o carte
        player.adauga_carte(pachet.trage_carte())  # adauga carte si actualizeaza scorul
        # 2.dealerul primeste o carte
        dealer.adauga_carte(pachet.trage_carte())
        # 3.playerul primeste o carte
        player.adauga_carte(pachet.trage_carte())
        # 4.dealerul primeste o carte
        dealer.adauga_carte(pachet.trage_carte())

        player.arata_mana()
        dealer.arata_mana(arata_o_carte=True)

        # handle player turn
        player_la_rand = True
        while player_la_rand:
            trage_sau_ramai = input("Vrei sa mai tragi o carte (apasa y) sau sa ramai (apasa n)? ")
            if trage_sau_ramai[0].lower() == 'y':
                print(f"{player.nume} mai trage o carte..")
                player.adauga_carte(pachet.trage_carte())
                player.arata_mana()
            elif trage_sau_ramai[0].lower() == 'n':
                print(f"{player.nume} ramane cu scorul de {player.scor}")
                player_la_rand = False
            else:
                print("Ai ales o optiune invalida!! Alege y (yes) sau n (no): ")

            if player.scor > 21:
                print(f"{player.nume} a trecut de 21!")
                player_la_rand = False

        # handle dealer turn
        if player.scor <= 21:
            dealer.arata_mana()
            while dealer.scor < 17:
                dealer.adauga_carte(pachet.trage_carte())
                dealer.arata_mana()

            # handle win cases
            if dealer.scor == player.scor:
                print(f"Egalitate")
                player.sold += pariu
            elif dealer.scor > player.scor and dealer.scor <= 21:
                print(f"{dealer.nume} a castigat!")
            else:
                print(f"{player.nume} a castigat!")
                player.sold += 2 * pariu
        else:
            print(f"{dealer.nume} a castigat!")

        # ask to play again
        mai_joci = input(f"{player.nume}, mai vrei sa joci o tura?? (y/n) ")
        while mai_joci[0].lower() not in ('y', 'n'):
            mai_joci = input(f"{player.nume}, mai vrei sa joci o tura?? (y/n) ")

        if mai_joci[0].lower() == 'n':
            break

    print(f"Multumesc pentru joc, {player.nume}!")


play_game()


# player primeste 1 carte
# dealer primeste 1 carte (fata in jos - ascunsa)
# player primeste 1 carte
# dealer primeste 1 carte

# Level 2: this is the mappings structures that you could use for setting suits and ranks and mapping of values

# define yourself a suits tuple containig the possible suits (Hearts, Clubs...)
# a ranks tuple with all the possible ranks (2, 3 .... K, A)
# and a rank_to_value structure
#suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')
#ranks = ('2', '3', '4', '5', '6', '7', '8',
         # '9', '10', 'J', 'Q', 'K', 'A')
#rank_to_value = {
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '10': 10,
#     'J': 10,
#     'Q': 10,
#     'K': 10,
#     'A': 11
# }


# Level 3: this is the main loop of the game
#def play_game():
    # initialize player and dealer

    #while True:


# initialize deck and players hands

# check if player has any chips to play a round and ask for a bet

# deal cards

# handle player turn

# handle dealer turn

# handle win cases

# ask to play again


# Imbunatatire in definirea claselor Player si Dealer prin folosirea mostenirii
class BasePlayer:
    def __init__(self, nume):
        self.nume = nume
        self.carti = []
        self.scor = 0
        self.nr_asi = 0

    # adauga carte si actualizeaza scorul
    def adauga_carte(self, carte_noua):
        print(f"{self.nume} a tras o carte.")
        self.carti.append(carte_noua)
        self.scor += carte_noua.punctaj
        if carte_noua.valoare == 'A':
            self.nr_asi += 1
        if len(self.carti) == 2 and self.scor == 22:  # cazul in care avem 2 de 'A' in mana, scorul trebuie sa fie 21!
            self.scor = 21
        while self.scor > 21 and self.nr_asi:  # ['A', 2] = 11 + 2 = 13  + carte_noua('K')  => 13 + 10 = 23 , dar avem 'A' in lista de carti => 23-10=13
            self.scor -= 10
            self.nr_asi -= 1

    def golire_mana(self):
        self.carti.clear()
        self.scor = 0

    def arata_mana(self, arata_o_carte=False):  # in cazul Player se cheama functia cu arata_o_carte=False mereu!
        if arata_o_carte:
            print(f"{self.nume} are in mana: {self.carti[0]} cu scorul: {self.carti[0].punctaj}")
        else:
            print(f"{self.nume} are in mana: {[str(c) for c in self.carti]} cu scorul: {self.scor}")


class Player(BasePlayer):
    def __init__(self, nume, sold):
        self.sold = sold
        super().__init__(nume)

    def __str__(self):
        return f"{self.nume} are soldul = {self.sold}"

    def verificare_sold(self):
        return self.sold > 0

    def pariaza(self):
        suma_pariata = int(input("Alege suma pariata: "))
        # tot cere input atata timp cat suma introdus e mai mare ca sold
        while self.sold < suma_pariata:
            print("Nu aveti destui bani!")
            suma_pariata = int(input("Alege suma pariata: "))

        self.sold -= suma_pariata
        return suma_pariata


class Dealer(BasePlayer):
    def __init__(self):
        super().__init__("Dealer")

    def __str__(self):
        return f"{self.nume}"

# Nu se modifica cu nimic functia play_game....

def play_game():
    """!Tip: Game will run in a while loop..."""
    # initialize player and dealer
    dealer = Dealer()

    nume_jucator = input("Introduceti numele jucatorului: ")
    sold = int(input("Alegeti suma de bani de pariat: "))
    player = Player(nume_jucator, sold)

    while True:
        # initialize deck and players hands (initializare pachet si mainile jucatorilor)
        pachet = Deck()
        pachet.amestecare_pachet()
        dealer.golire_mana()
        player.golire_mana()

        print(player)

        # check if player has any chips to play a round and ask for a bet (verificare sold jucator si interogare pariu)
        if not player.verificare_sold():
            print(f"{player.nume} nu mai are bani :(... Multumim de bani!")
            break

        pariu = player.pariaza()

        # deal cards
        # 1.playerul primeste o carte
        player.adauga_carte(pachet.trage_carte())  # adauga carte si actualizeaza scorul
        # 2.dealerul primeste o carte
        dealer.adauga_carte(pachet.trage_carte())
        # 3.playerul primeste o carte
        player.adauga_carte(pachet.trage_carte())
        # 4.dealerul primeste o carte
        dealer.adauga_carte(pachet.trage_carte())

        player.arata_mana()
        dealer.arata_mana(arata_o_carte=True)

        # handle player turn
        player_la_rand = True
        while player_la_rand:
            trage_sau_ramai = input("Vrei sa mai tragi o carte (apasa y) sau sa ramai (apasa n)? ")
            if trage_sau_ramai[0].lower() == 'y':
                print(f"{player.nume} mai trage o carte..")
                player.adauga_carte(pachet.trage_carte())
                player.arata_mana()
            elif trage_sau_ramai[0].lower() == 'n':
                print(f"{player.nume} ramane cu scorul de {player.scor}")
                player_la_rand = False
            else:
                print("Ai ales o optiune invalida!! Alege y (yes) sau n (no): ")

            if player.scor > 21:
                print(f"{player.nume} a trecut de 21!")
                player_la_rand = False

        # handle dealer turn
        if player.scor <= 21:
            dealer.arata_mana()
            while dealer.scor < 17:
                dealer.adauga_carte(pachet.trage_carte())
                dealer.arata_mana()

            # handle win cases
            if dealer.scor == player.scor:
                print(f"Egalitate")
                player.sold += pariu
            elif dealer.scor > player.scor and dealer.scor <= 21:
                print(f"{dealer.nume} a castigat!")
            else:
                print(f"{player.nume} a castigat!")
                player.sold += 2 * pariu
        else:
            print(f"{dealer.nume} a castigat!")

        # ask to play again
        mai_joci = input(f"{player.nume}, mai vrei sa joci o tura?? (y/n) ")
        while mai_joci[0].lower() not in ('y', 'n'):
            mai_joci = input(f"{player.nume}, mai vrei sa joci o tura?? (y/n) ")

        if mai_joci[0].lower() == 'n':
            break

    print(f"Multumesc pentru joc, {player.nume}!")

play_game()