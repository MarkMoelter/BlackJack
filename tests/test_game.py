import unittest

from cards import Card, Suite, Value
from game import Game, Player


class TestGameMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.mark_player = Player('Mark')
        self.single_player = Game([self.mark_player])

    def test_award_winner(self):
        # setup
        ace = Card(Suite.HEART, Value.ACE)
        nine = Card(Suite.HEART, Value.NINE)
        eight = Card(Suite.HEART, Value.EIGHT)

        ### push ###
        self.single_player.dealer.hand = [ace, nine]

        self.mark_player.balance = 100
        self.mark_player.bet(15)
        self.mark_player.hand = [ace, nine]

        self.single_player.award_winner(self.mark_player)
        self.assertEqual(self.mark_player.balance, 100)

        ### win ###
        self.single_player.dealer.hand = [ace, eight]

        self.mark_player.balance = 100
        self.mark_player.bet(15)
        self.mark_player.hand = [ace, nine]

        self.single_player.award_winner(self.mark_player)
        self.assertEqual(self.mark_player.balance, 115)

        ### lose ###
        self.single_player.dealer.hand = [ace, nine]

        self.mark_player.balance = 100
        self.mark_player.bet(15)
        self.mark_player.hand = [ace, eight]

        self.single_player.award_winner(self.mark_player)
        self.assertEqual(self.mark_player.balance, 85)

    def test_hit(self):
        self.single_player.hit(self.mark_player)
        self.assertEqual(len(self.mark_player.hand), 1, 'Should be 1...')

        self.single_player.hit(self.mark_player)
        self.single_player.hit(self.mark_player)
        self.assertEqual(len(self.mark_player.hand), 3, 'Should be 3...')

    def test_double_down(self):
        self.mark_player.bet_amount = 15
        self.assertEqual(self.mark_player.bet_amount, 15, 'Should be 15...')

        self.single_player.double_down(self.mark_player)
        self.assertEqual(self.mark_player.bet_amount, 30, 'Should be 30...')
        self.assertEqual(len(self.mark_player.hand), 1, 'Should be 1...')


if __name__ == '__main__':
    unittest.main()
