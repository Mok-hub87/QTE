n=int(input())
m=int(input())
k=int(input())
s=n*m
if k%n==0 or k%m==0 and k<s:
    print("yes")
else:
    print("no")
