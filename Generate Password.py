import random
passlen = int(input("Enter the length of password:"))
x = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
y = "".join(random.sample(x,passlen ))
print(y)