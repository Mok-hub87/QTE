a=int(input())+1
b=int(input())
s=[]
while a>b:
    d=a%2
    a-=1
    if d==0:
        s.append(a)
        if a==b:
            print(s)
            