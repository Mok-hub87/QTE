n=int(input())
a=0
s=[]
while a<n:
    f=a**2
    s.append(f)
    a+=1
    if a==n:
        print(s)
