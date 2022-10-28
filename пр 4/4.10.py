n=int(input())
k=int(input())
f1=1
f2=1
a=[]
for i in range(1,n-1):
    f1,f2=f2,f1+f2
    a.append(f2)
w=a[k-1:n]
s=sum(w)
print(s)
print(w)
