q=int(input())
w=1
e=0
while q!=0:
    a=int(input())
    q,a=a,q
    if a==q:
        w+=1
    if w>e:
        e=w
    if q!=a:
        w=1
print(e)
