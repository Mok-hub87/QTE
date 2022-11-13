import random
n=int(input())
m=int(input())
b=[[random.randrange(10)for i in range(m)]for j in range(n)]
for i,s in enumerate(b):
    max=min=0
    for j,a in enumerate(s):
        if a>s[max]:
            max=j
        if a<s[min]:
            min=j
    s[max],s[0]=s[0],s[max]
    s[min],s[-1]=s[-1],s[min]
print(b)
