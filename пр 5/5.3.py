n=int(input())
q=0
w=0
while 2**q<=n:
    w=2**q
    q+=1
print(q-1,w)
