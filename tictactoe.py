import random
from linkedbst import LinkedBST
from TreeNode import Node

class Board:
    WINNER = None

    def __init__(self):
        self.coordinates = [None for i in range(9)]

    def set_mark(self, symbol, coordinate):
        self.coordinates[coordinate] = symbol

    def tie(self):
        if not self.is_winner() and None not in self.coordinates:
            self.WINNER = 'TIE'
            return True
        return False

    def is_winner(self):
        for i in range(3):
            if self.coordinates[i] == self.coordinates[i + 3] == self.coordinates[i + 6]:
                self.WINNER = self.coordinates[i]
                if self.WINNER:
                    return True

        for i in range(3):
            if self.coordinates[i * 3] == self.coordinates[i * 3 + 1] == self.coordinates[i * 3 + 2]:
                self.WINNER = self.coordinates[i * 3]
                if self.WINNER:
                    return True

        for i in range(2):
            if self.coordinates[2 * i] == self.coordinates[4] == self.coordinates[i * 2 + 6]:
                self.WINNER = self.coordinates[i * 2]
                if self.WINNER:
                    return True

        return False

    def __str__(self):
        r = ''
        for i in range(9):
            if i%3 == 0:
                r += '\n'
            line = self.coordinates[i]
            if line:
                r += ' ' + line + ' '
            else:
                r += ' ' + '□' + ' '

        return r



class Bot:
    SYMBOL = 'O'
    def __init__(self, board):
        self.board = board

    def fill_tree(self):
        tree = LinkedBST()
        node = Node(self.board)
        print(node)
        for i in range(9):

            if self.board.coordinates[i] is None:
                self.board.coordinates[i] = 'X'
                node.add_child((self.board))
                self.board.coordinates[i] = None
                #print(1, node)
        tree.add(node)


    def make_move(self, board):
        move = random.randint(0, 8)
        while board.coordinates[move] is not None:
            move = random.randint(0, 8)
        board.set_mark(self.SYMBOL, move)


class Player:
    SYMBOL = 'X'

    def make_move(self, board):
        move = int(input("Please enter the position you want to place a symbol: "))
        while board.coordinates[move] is not None and 0 <= move < 9:
            move = int(input("Please enter the position you want to place a symbol: "))
        board.set_mark(self.SYMBOL, move)


def play():
    b = Board()
    a = Bot(b)
    aa = Player()
    while not b.is_winner() and not b.tie():
        a.make_move(b)
        print(b)
        if not b.is_winner() and not b.tie():
            aa.make_move(b)
            print(b)
    print(b.WINNER)
a = Board()
b = Bot(a)
b.make_move(a)
b.fill_tree()
