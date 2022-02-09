player = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],]


def player_board():
    print("   0  1  2")
    for count, lines in enumerate(player):        
        print(count, lines)

player_board()
player[0][1] = 1
player_board()

