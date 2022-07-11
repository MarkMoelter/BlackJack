import unittest

from Cards import Card, Value, Suite
from Game import Rules


class TestRules(unittest.TestCase):

    def setUp(self):
        # blackjack Cards
        self.ace_king = Rules(
            [
                Card(Suite.HEART, Value.ACE),
                Card(Suite.HEART, Value.KING)
            ]
        )

        self.ace_eight_king = Rules(
            [
                Card(Suite.HEART, Value.ACE),
                Card(Suite.HEART, Value.EIGHT),
                Card(Suite.HEART, Value.KING)
            ]
        )

        self.king_eight_king = Rules(
            [
                Card(Suite.HEART, Value.KING),
                Card(Suite.HEART, Value.EIGHT),
                Card(Suite.HEART, Value.KING)
            ]
        )

    def test_is_blackjack(self):
        #
        self.assertTrue(
            self.ace_king.is_blackjack(),
            'Should be true...'
        )

        self.assertFalse(
            self.king_eight_king.is_blackjack(),
            'Should be false...'
        )

        self.assertFalse(
            self.ace_eight_king.is_blackjack(),
            'Should be false...'
        )

    def test_bust(self):
        self.assertTrue(
            self.king_eight_king.is_bust(),
            'Should be true...'
        )

        self.assertFalse(
            self.ace_king.is_bust(),
            'Should be false...'
        )

        self.assertFalse(
            self.ace_eight_king.is_bust(),
            'Should be false...'
        )

    def test_value(self):
        # test the hand_value method
        self.assertEqual(
            self.ace_king.hand_value(),
            21,
            'Should be 21...'
        )

        self.assertEqual(
            self.king_eight_king.hand_value(),
            28,
            'Should be 28...'
        )

        self.assertEqual(
            self.ace_eight_king.hand_value(),
            19,
            'Should be 19...'
        )


if __name__ == '__main__':
    unittest.main()
