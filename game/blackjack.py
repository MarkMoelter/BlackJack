from cards import Shoe
from .dealer import Dealer
from .player import Player
from .rules import Rules

START_CARD_NUMBER = 2


class BlackJack:
    def __init__(
            self,
            players: list[Player],
            dealer: Dealer = Dealer()):
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

        print(f"Dealer's hand: {self.dealer.hand}")
        print(f"Dealer's value: {Rules(self.dealer).hand_value()}")

        for player in self.players:
            self.award_winner(player)
            print(f"{player.name}'s final balance: {player.balance}")

    def award_winner(self, player: Player):
        """Rules for determining the winner of the game.
         Deposits the bet amount into the balance."""
        win = Rules(player).hand_value() > Rules(self.dealer).hand_value()
        push = Rules(player).hand_value() == Rules(self.dealer).hand_value()

        dealer_bust = Rules(self.dealer).is_bust()
        player_bust = Rules(player).is_bust()

        if (dealer_bust and not player_bust) or win:
            # return the bet twofold
            player.deposit(player.bet_amount * 2)
            print(f'{player.name} won! Earned {player.bet_amount}')
        elif push:
            # return the bet to the player' balance.
            player.deposit(player.bet_amount)
            print(f'{player.name} pushed!')
        else:
            print(f'{player.name} lost!')

        player.bet_amount = 0

    def player_turn(self, player: Player):
        """Player's turn"""
        while True:
            # print the player's cards
            print(f"{player.name}'s turn")
            print(player.hand)
            value = Rules(player).hand_value()
            print(f'Hand value: {value}')

            # give the option to stay, hit, double down, or split
            options = {
                'hit': self.hit,
                'double down': self.double_down,
                'split': self.split
            }

            player_choice = input('"stay", "hit", "double down", "split": ')
            if player_choice == 'stay':
                return

            options[player_choice](player)

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
        # hit if under 17
        while Rules(self.dealer).hand_value() < 17:
            self.dealer.add_cards(self.shoe.deal())
        return

    def game_initial_setup(self):
        """Deal starting cards"""
        for player in self.players:
            player.bet(int(input(f'{player.name}, enter your bet: ')))

        # give 2 cards to start
        for _ in range(START_CARD_NUMBER):
            # dealer cards
            self.dealer.hand.append(self.shoe.deal())

            # player cards
            for player in self.players:
                player.hand.append(self.shoe.deal())
                if Rules(player).is_blackjack():
                    player.deposit(int(player.bet_amount * 1.5))
                    print(f"{player.name} got blackjack!")
