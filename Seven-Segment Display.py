def mat(m):
   x = 0
   match={
          "0": 6, "1": 2,"2":5, "3": 5,

          "4": 4, "5": 5, "6": 6,

          "7": 3, "8": 7,"9": 6 }
   for i in m :
       x += match[i]
   r = x % 2
   result = ["1"]
   if r == 0 :
       result.append(x // 2)
       result.append("")
   elif r == 1:
       result.append((x // 2)-1)
       result.append("7")
   return ((result[0] * result[1]) + result[2])
n = int(input())
while n!=0:
   m = input()
   print(mat(m)[::-1])
   n = n-1