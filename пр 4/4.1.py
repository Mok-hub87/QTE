a=int(input())
b=int(input())+1
s=[]
while a<=b:
    s.append(a)
    a=a+1
    if b==a:
        print(s)
