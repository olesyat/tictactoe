from node_tree import Node, Tree
from copy import deepcopy

class Board:
    WINNER = None

    def __init__(self):
        self.coordinates = [None for i in range(9)]
        self.last_value = None
        self.last_position = None

    def set_mark(self, symbol, coordinate):
        self.coordinates[coordinate] = symbol
        self.last_value = symbol
        self.last_position = coordinate

    def tie(self):
        if not self.is_winner() and None not in self.coordinates:
            self.WINNER = 'TIE'
            return True
        return False

    def is_winner(self):
        for i in range(3):
            if self.coordinates[i] == self.coordinates[i + 3] == self.coordinates[i + 6]:
                Board.WINNER = self.coordinates[i]
                if Board.WINNER:
                    return True

        for i in range(3):
            if self.coordinates[i * 3] == self.coordinates[i * 3 + 1] == self.coordinates[i * 3 + 2]:
                Board.WINNER = self.coordinates[i * 3]
                if Board.WINNER:
                    return True

        for i in range(2):
            if self.coordinates[2 * i] == self.coordinates[4] == self.coordinates[8 - 2*i]:
                Board.WINNER = self.coordinates[4]
                if Board.WINNER:
                    return True

        return False

    def __str__(self):
        r = ''
        for i in range(9):
            if i % 3 == 0:
                r += '\n'
            line = self.coordinates[i]
            if line:
                r += ' ' + line + ' '
            else:
                r += ' ' + '□' + ' '

        return r


class Player:
    SYMBOL = 'X'
    def __init__(self, board):
        self.board = board

    def make_move(self):
        move = int(input("Please enter the position you want to place a symbol: "))
        while self.board.coordinates[move] is not None and 0 <= move < 9:
            move = int(input("Please enter the position you want to place a symbol: "))
        self.board.set_mark(self.SYMBOL, move)

class Bot:
    SYMBOL = 'O'
    def __init__(self, board):
        self.board = board
        self.TREE = None

    def fill_tree(self):
        self.TREE = Tree(Node(self.board, None))
        def helper(node):
            for j in range(9):
                if node.data.coordinates[j] is None:
                    prototype = deepcopy(node.data)
                    if prototype.last_value == 'X':
                        prototype.set_mark('O', j)
                        prototype.last_position = j
                    elif prototype.last_value == 'O':
                        prototype.set_mark('X', j)
                        prototype.last_position = j
                    else:
                        prototype.set_mark('X', j)
                        prototype.last_position = j

                    _child = Node(prototype, node)
                    node.add_child(_child)

                    if prototype.tie():
                        pass

                    elif not prototype.is_winner():
                        helper(_child)
                    else:

                        if Board.WINNER == 'X':
                            node.chance -= 1
                        if Board.WINNER == 'O':
                             node.chance += 1



        helper(self.TREE._root)
        options = []
        for t in self.TREE._root.children:
            options.append(t.count_chance())
        answer = max(options)
        ans = self.TREE._root.children[options.index(answer)].data
        return ans.last_position

    def make_move(self):
        move = self.fill_tree()
        self.board.set_mark(self.SYMBOL, move)