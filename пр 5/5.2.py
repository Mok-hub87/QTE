n=int(input())
f=0
s=[]
for i in range (2,n):
    if n%i==0:
        s.append(i)
        print(s[0])
