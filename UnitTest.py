import unittest
from PokerMachine import *


class TestPokerMachine(unittest.TestCase):
    def testHandAmount(self, handAmount):

        hand = drawRandomCards(handAmount)
        self.assertEqual(len(hand[0]), handAmount) , "Hand Amount is not correct! Something went wrong!"

    def testSort(self, handAmount):
        hand = drawRandomCards(handAmount)
        hand = sortCards(hand)
        self.assertEqual(hand, sorted(hand)), "Hand is not sorted! Something went wrong!"

if __name__ == "__main__":
    unittest.main(8)