game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def tictactoe(player=0, row=0, column=0, just_display=False):
    print("   0  1  2")
    if not just_display:
        game[row][column] = player
    for count, lines in enumerate(game):
        print(count, lines)

tictactoe()
