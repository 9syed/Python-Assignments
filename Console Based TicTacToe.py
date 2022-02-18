game = [[2, 0, 1],
		[2, 0, 0],
		[2, 2, 0],]
		
for col in range(len(game)):
    check = []

    for line in game:
        check.append(line[0])
        
    if check.count(check[0]) == len(check) and check[0] != 0:
        print("Winner!")


'''def win(current_game):
    for line in game:
        print(line)
        not_match = False
        for element in line:
            if element != line[0]:
                not_match == True
        if not not_match:
            print("Winner!")

win(game)'''