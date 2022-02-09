L,R,K=input().split()
 
def c(l,r,k):
    l=int(L)
    r=int(R)
    k=int(K)
    c=0
    for i in range(l,r+1):
        if i%k==0:
            c+=1
    return c
print(c(L,R,K))