input_string = input()

total_length = len(input_string)
z_count = 0
o_count = 0

for eachCharacter in input_string:
    if eachCharacter == 'z' or eachCharacter == 'Z':
        z_count = z_count +1
    if eachCharacter == 'o' or eachCharacter == 'O':
        o_count = o_count +1

if z_count == o_count/2:
    print("Yes")
else:
    print("No")