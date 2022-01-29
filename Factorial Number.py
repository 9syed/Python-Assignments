# Python program to find the factorial of a number.
#number = int(input("Enter a number: "))

number = int(input())
factorial = 1

if number < 0:
   print("Factorial do not exist for negative numbers!")
elif number == 0:
   print("1")
else:
   for i in range(1, number + 1):
       factorial = factorial*i
   print(factorial)

#fn=int(input())

