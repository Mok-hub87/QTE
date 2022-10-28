n=int(input())
f=1
a=[]
t=0
for i in range(1,n+1):
    f=f*i
    a.append(f)
t=sum(a)
print(t)

