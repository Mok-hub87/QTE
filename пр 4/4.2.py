a=int(input())
b=int(input())
s=[]
while a<b or a>b:
    if a<b:
        s.append(a)
        a+=1
        if a==b:
            print(" ".join(map(str,s)),b)
    elif b<a:
        s.append(a)
        a-=1
        if a==b:
            print(" ".join(map(str,s)),a)
            