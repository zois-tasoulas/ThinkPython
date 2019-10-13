"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

from Card import Hand, Deck


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False

    def has_two_pair(self):
        """Returns True if the hand has two pairs, False otherwise."""
        cnt = 0
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                cnt += 1
        return cnt >= 2

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise."""
        self.sort()    #Sort again to avoid errors in case of omission
        seq = 1
        mxm = 0
        prevCard = self.cards[0].rank
        for card in self.cards[1:]:
            if card.rank == prevCard + 1:
                seq += 1
            elif card.rank == prevCard:
                #if we have cards with the same rank, seq should not change
                pass
            else:
                seq = 1
            prevCard = card.rank
            if seq > mxm:
               mxm = seq
        #Check the case of a 10-Jack-Queen-King-Ace straight
        if mxm == 4 and seq == 4 and self.cards[0].rank == 1 and self.cards[-1].rank == 13:
            mxm = 5
        return mxm >= 5

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.

        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise."""
        return (self.has_three_of_a_kind() and self.has_two_pair())

    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind, False otherwise."""
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 4:
                return True
        return False

    def hand_with_specific_suit(self, suit):
        new_hand = PokerHand()
        for card in self.cards:
            if card.suit == suit:
                new_hand.add_card(card)
        return new_hand

    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise."""
        clubs_hand = self.hand_with_specific_suit(0)
        if len(clubs_hand.cards) > 4 and clubs_hand.has_straight():
            return True
        diamonds_hand = self.hand_with_specific_suit(1)
        if len(diamonds_hand.cards) > 4 and diamonds_hand.has_straight():
            return True
        hearts_hand = self.hand_with_specific_suit(2)
        if len(hearts_hand.cards) > 4 and hearts_hand.has_straight():
            return True
        spades_hand = self.hand_with_specific_suit(3)
        if len(spades_hand.cards) > 4 and spades_hand.has_straight():
            return True
        return False

    def classify(self):
        if self.has_straight_flush():
            self.label = "straight flush"
        elif self.has_four_of_a_kind():
            self.label = "four of a kind"
        elif self.has_full_house():
            self.label = "full house"
        elif self.has_flush():
            self.label = "flush"
        elif self.has_straight():
            self.label = "straight"
        elif self.has_three_of_a_kind():
            self.label = "three of a kind"
        elif self.has_two_pair():
            self.label = "two pair"
        elif self.has_pair():
            self.label = "pair"
        else:
            self.label = "no combination"

def statistics():
    hands = {}
    iterations = 500
    number_of_hands = 7
    for j in range(iterations):
        deck = Deck()
        deck.shuffle()
        for i in range(number_of_hands):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            #print(hand)
            #print('')
            hand.classify()
            hands[hand.label] = hands.get(hand.label, 0) + 1
    for key in sorted(hands):
        print("Probability of a %s is %.3f%%" % (key, hands[key] / (iterations * number_of_hands) * 100))

if __name__ == '__main__':
    statistics()
