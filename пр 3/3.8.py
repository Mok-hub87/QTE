a=int(input())
b=int(input())
c=int(input())
if a==b and b==c and c==a:
    print(3)
elif (a==b and c!=a) or (a!=b and b==c) or (b!=c and c==a):
    print(2)
elif a!=b and b!=c and c!=a:
    print(0)
    