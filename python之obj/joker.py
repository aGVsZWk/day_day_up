# 扑克牌初始化
import abc
import random


class Card:
    """卡牌基类."""

    def __init__(self, rank, suit):
        """
        :param rank: 大小.
        :type rank: str
        :param suit: 花色.
        :type suit: str
        """
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    """数字牌."""

    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    """A. 1点或11点"""

    def _points(self):
        return 1, 11


class FaceCard(Card):
    """JQK. 10点"""

    def _points(self):
        return 10, 10


class Suit:
    """花色.

    :param name: 名称.
    :type name: str
    :param symbol: 符号.
    :type symbol: str
    >> Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
    """

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class CardFactory(object):
    """卡牌工厂.
    >> card8 = CardFactory()
    >> deck8 = [card8.rank(r+1).suit(s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]
    """

    def rank(self, rank):
        """创建点数.
        :param rank: 大小.
        :type rank: int
        """
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self

    def suit(self, suit):
        """创建花色.

        :param suit: 花色.
        :type suit: Suit
        """
        return self.class_(self.rank_str, suit)


def card(rank, suit):
    """发牌.

    :param rank: 大小.
    :type rank: int
    :param suit: 花色.
    :type suit: Suit
    :return: 扑克牌.
    :rtype: Card

    """
    if rank == 1:
        return AceCard(rank, suit)
    elif 2 <= rank < 11:
        return NumberCard(rank, suit)
    elif 11 <= rank < 14:
        return FaceCard(rank, suit)
    else:
        raise Exception("Rank out of range")


# class Deck:
#     """洗牌, 发牌.
#     """
#     def __init__(self):
#         self._cards = [card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]
#         random.shuffle(self._cards)
#
#     def pop(self):
#         return self._cards.pop()


# class Deck(list):
#     def __init__(self):
#         super().__init__(card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
#         random.shuffle(self)


class Deck(list):
    def __init__(self, decks=1):
        """Short summary.

        :param decks: 几副牌混在一起.
        :type decks: int

        """
        super().__init__()
        for i in range(decks):
            self.extend(card(r + 1, s) for r in ragne(13) for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(born):
            self.pop()


# class Hand:
#     def __init__(self, dealer_card):
#         self.dealer_card = dealer_card
#         self.cards = []
#
#     def hard_total(self):
#         return sum(c.hard for c in self.cards)
#
#     def soft_total(self):
#         return sum(c.soft for c in self.cards)


# class Hand:
#     """打牌策略.
#
#     :param dealer_card: 要处理的牌.
#     :type dealer_card: Card
#     :param *cards: 手中的牌.
#     :type *cards: Card
#     >> d = Deck()
#     >> h = Hand(d.pop(), d.pop(), d.pop())
#     """
#
#     def __init__(self, dealer_card, *cards):
#         self.dealer_card = dealer_card
#         self.cards = list(cards)
#
#     def hard_total(self):
#         return sum(c.hard for c in self.cards)
#
#     def soft_total(self):
#         return sum(c.soft for c in self.cards)
#
#
# class Hand:
#     def __init__(self, *args, **kw):
#         if len(args) == 1 and isinstance(args[0], Hand):
#             other = args[0]
#             self.deal_card = other.deal_card
#             self.cards = other.cards
#         elif len(args) == 2 and isinstance(args[0], Hand) and 'split' in kw:
#             other, card = args
#             self.deal_card = other.deal_card
#             self.cards = list(cards)
#         elif len(args) == 3:
#             deal_card, *cards = args
#             self.cards = list(cards)
#         else:
#             raise TypeError("Invalid constructor args={0!r} kw={1!r}".format(args, kw))
#
#     def __str__(self):
#         return ", ".join(map(str, self.cards))


class Hand:
    """打牌策略.

    :param dealer_card: 要处理的牌.
    :type dealer_card: Card
    :param *cards: 手中的牌.
    :type *cards: Card
    >> d = Deck()
    >> h = Hand(d.pop(), d.pop(), d.pop())
    """
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = cards

    @staticmethod
    def freeze(other):
        hand = Hand(other.dealer_card, *other.cards)
        return hand

    @staticmethod
    def split(other, card0, card1):
        hand0 = Hand(other.dealer_card, other.cards[0], card0)
        hand1 = Hand(other.dealer_card, other.cards[1], card1)
        return hand0, hand1

    def __str__(self):
        return ", ".join(map(str, self.cards))


class GameStragegy:
    """游戏模式.
    >> dumb = GameStratege()
    """

    def insurance(self, hand):
        return False

    def split(self, hand):
        return False

    def double(self, hand):
        return False

    def hit(self, hand):
        return False


class Table:
    """模拟器.
    """
    def __init__(self):
        self.deck = Deck()

    def place_bet(self, amount):
        print("Bet", amount)

    def get_hand(self):
        try:
            self.hand = Hand(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except IndexError:
            self.deck = Deck()
            return self.hand
        print("Deal", send.hand)
        return self.hand

    def can_insure(self, hand):
        return hand.dealer_card.insure


class BettingStragegy(abc.ABCMeta):
    """下注策略."""
    @abc.abstractmethod
    def bet(self):
        raise NotImplementedError("No bet method")

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Flat(BettingStragegy):
    def bet(self):
        return 1


class Player(Player):
    def __init__(self, table, bet_strategy, game_strategy, **extras):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table = table
        self.__dict__.update(extras)
