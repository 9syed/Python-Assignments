t = int(input())
A = input()
A = A.split(' ')

y = []
for i in range(len(A)//2):
    y.append(A[i][0])
for i in range(len(A)//2, len(A), 1):
    y.append(A[i][len(A[i])-1])


y = ''.join(y)

if int(y)%11==0:
    print("OUI")
else:
    print("NON")