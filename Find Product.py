def find_product(input_list):
    i = 0
    answer = 1
    while i < len(input_list):
        answer = (answer * int(input_list[i])) % (10**9 + 7)
        i+= 1

    print (answer)
list_size = input()
input_list = list(map(int,input().split()))

find_product(input_list)