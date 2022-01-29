# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

x = int(input("Enter a number: "))
if (x % 2) == 0:
   print(x, "is an Even number")
else:
   print(x, "is an Odd number")