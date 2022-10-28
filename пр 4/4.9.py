n=int(input())
a1=1
a2=1
q=0
a=[]
while q<n-2:
    asum=a1+a2
    a1=a2
    a2=asum
    q=q+1
    a.append(a2)
alist=sum(a)
print(alist)
