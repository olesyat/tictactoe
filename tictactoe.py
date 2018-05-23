import random
from node_tree import Node, Tree
from copy import deepcopy
from tic_tac import Board, Player

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

                    fucking_child = Node(prototype, node)
                    node.add_child(fucking_child)

                    if prototype.tie():
                        pass

                    elif not prototype.is_winner():
                        helper(fucking_child)
                    else:

                        if Board.WINNER == 'X':
                            node.chance -= 1
                        if Board.WINNER == 'O':
                             node.chance += 1



        helper(self.TREE._root)
        options = []
        for t in self.TREE._root.children:
            options.append(t.count_chance())
        print(options)
        answer = max(options)
        ans = self.TREE._root.children[options.index(answer)].data
        #print('informal', ans, ans.last_position)
        # print(ans)
        # print(Bot.P, Bot.BOT)
        return ans.last_position

    def make_move(self):
        move = self.fill_tree()
        self.board.set_mark(self.SYMBOL, move)


def play():
    b = Board()
    bot = Bot(b)
    player = Player(b)
    while not b.is_winner() and not b.tie():
        player.make_move()
        print(b)
        if not b.is_winner() and not b.tie():
            bot.make_move()
            print(b)
    print("WINNER", b.WINNER)
play()
#
# a = Board()
# b = Bot(a)
# r = Player(a)
# r.make_move()
# b.make_move()

