from cards import Shoe
from .dealer import Dealer
from .player import Player
from .rules import Rules

START_CARD_NUMBER = 2


class Game:
    def __init__(self, players: list[Player], dealer: Dealer = Dealer()):
        self.players = players
        self.dealer = dealer
        self.shoe = Shoe()

    def single_game(self):
        """Implement a single game of BlackJack."""

        self.game_initial_setup()

        for player in self.players:
            if Rules(player).is_blackjack():
                continue
            self.player_turn(player)

        self.dealer_turn()

        for player in self.players:
            self.award_winner(player)

    def award_winner(self, player):
        win = Rules(player).hand_value() > Rules(self.dealer).hand_value()
        push = Rules(player).hand_value() == Rules(self.dealer).hand_value()

        if win:
            # return the bet twofold
            player.deposit(player.bet_amount * 2)
        elif push:
            # return the bet
            player.deposit(player.bet_amount)

        player.bet_amount = 0

    def player_turn(self, player):
        """Player's turn"""
        while True:
            # print the player's cards
            print(player.hand)
            value = Rules(player).hand_value()
            print(f'Hand value: {value}')

            # give the option to stay, hit, double down, or split
            options = {
                'hit': self.hit(player),
                'double down': self.double_down(player),
                'split': self.split(player)
            }

            player_choice = input('"stay", "hit", "double down", "split": ')
            if player_choice == 'stay':
                return

            selection = options[player_choice]

            # check if busted
            if Rules(player).is_bust():
                player.clear_hand()
                return

    def hit(self, player: Player):
        """Draw a card from the shoe."""
        # deal card
        player.add_cards(self.shoe.deal())

    def double_down(self, player: Player):
        """Double your bet and draw a card."""
        # double the bet
        player.bet(player.bet_amount)
        player.add_cards(self.shoe.deal())

    def split(self, player: Player):
        """Keep track of two hands for 1 player."""
        raise NotImplementedError

    def dealer_turn(self):
        """Dealer rules"""
        raise NotImplementedError

    def game_initial_setup(self):
        """Deal starting cards"""
        for player in self.players:
            player.bet(int(input('Enter your bet: ')))

        # give 2 cards to start
        for _ in range(START_CARD_NUMBER):
            # dealer cards
            self.dealer.hand = self.shoe.deal()

            # player cards
            for player in self.players:
                player.hand.append(self.shoe.deal())
                if Rules(player).is_blackjack():
                    player.deposit(int(player.bet_amount * 1.5))
