def numberofstring(x, y, z, col, hay, row_max, col_max):
	
	found = 0
	if (z >= 0 and z <= row_max and
		col >= 0 and col <= col_max and
		y[x] == hay[z][col]):
		match = y[x]
		x += 1
		hay[z][col] = 0
		if (y == len(y)):
			found = 1
		else:
			found += numberofstring(x, y, z, col + 1, hay, row_max, col_max)
			found += numberofstring(x, y, z, col - 1, hay, row_max, col_max)
			found += numberofstring(x, y, z + 1, col, hay, row_max, col_max)
			found += numberofstring(x, y, z - 1, col, hay, row_max, col_max)

		hay[z][col] = match
	return found

def character2d(needle, row, col, str, row_count, col_count):
	found = 0
	for r in range(row_count):
		for c in range(col_count):
			found += numberofstring(0, needle, r, c, str, row_count - 1, col_count - 1)
	return found

needle = "MAGIC"
inputt = [[D,D,D,G,D,D],
          [B,B,D,E,B,S],
          [B,S,K,E,B,K],
          [D,D,D,D,D,E],
          [D,D,D,D,D,E],
          [D,D,D,D,D,G]]

str = [0] * len(inputt)

for i in range(len(inputt)):
	str[i] = list(inputt[i])
	
print("count: ", character2d(needle, 0, 0, str, len(str), len(str[0])))