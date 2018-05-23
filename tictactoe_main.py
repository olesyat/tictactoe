from tic_tac import Board, Player, Bot


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
