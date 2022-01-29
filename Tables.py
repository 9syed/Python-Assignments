table = int(input("Enter the table number: "))
print("The Multiplication Table of: ", table)


for row in range(1, 11):
   print(table, 'x', row, '=', table * row)