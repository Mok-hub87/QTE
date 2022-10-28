q=int(input())
a=0
w=[]
while q!=0:
    a+=1
    w.append(q)
    q=int(input())
e=sum(w)/len(w)
print(w)
print(e)
