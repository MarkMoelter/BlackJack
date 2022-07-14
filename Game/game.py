from Cards import Shoe
from .dealer import Dealer
from .player import Player
from .rules import Rules

START_CARD_NUMBER = 2


class Game:
    def __init__(self, players: list[Player], dealer: Dealer):
        self.players = players
        self.dealer = dealer
        self.shoe = Shoe()

    def show_players(self):
        for player in self.players:
            print(player)

    def single_game(self):
        """Implement the game loop"""

        # bets and deal cards
        self.card_setup()

        # each player's turn
        for player in self.players:
            self.turn(player)

        # todo dealer hit and stay

        # award the winners
        for player in self.players:
            # determine the winners
            self.determine_winner(player, self.dealer)

            # reset the bet parameter
            player.bet = 0

    @staticmethod
    def determine_winner(player, dealer):
        win = Rules(player).hand_value() > Rules(dealer).hand_value()
        tie = Rules(player).hand_value() == Rules(dealer).hand_value()
        if win:
            # return the bet twofold
            player.deposit(player.bet * 2)
        elif tie:
            # return the bet
            player.deposit(player.bet)

    def turn(self, player):
        """Player's turn"""
        while True:
            # check for blackjack
            if Rules(player).is_blackjack():
                return

            # print the player's cards
            print(player.hand)
            print(Rules(player).hand_value())

            # give the option to stay, hit, double down, or split
            choice = input('"stay", "hit", "double down", "split": ')

            if choice == 'stay':
                return

            elif choice == 'hit':
                # deal card
                player.hand = self.shoe.deal()

                # check if busted
                if Rules(player).is_bust():
                    player.clear_hand()
                    return

            elif choice == 'double down':
                # double the bet
                player.bet(player.bet)
                player.hand = self.shoe.deal()
                if Rules(player).is_bust():
                    player.clear_hand()
                return None

            elif choice == 'split':
                # todo split not yet supported, works like stay atm
                return

            else:
                print('Invalid choice...')

    def card_setup(self):
        """Deal starting cards"""

        # betting
        for player in self.players:
            bet = int(input('Enter your bet: '))
            player.bet(bet)

        # give 2 cards to start
        for _ in range(START_CARD_NUMBER):
            # dealer cards
            self.dealer.hand = self.shoe.deal()

            # player cards
            for player in self.players:
                player.hand = self.shoe.deal()
                rules = Rules(player)

                # blackjack
                if rules.is_blackjack():
                    player.deposit(int(player.bet * 1.5))
