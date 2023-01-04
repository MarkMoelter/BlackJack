import unittest

from cards import Card, Value, Suite


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = Card(Suite.CLUB, Value.ACE)

    def test_value(self) -> None:
        self.assertEqual(self.card.value, Value.ACE)

    def test_suite(self) -> None:
        self.assertEqual(self.card.suite, Suite.CLUB)


if __name__ == '__main__':
    unittest.main()
