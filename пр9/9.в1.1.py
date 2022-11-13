n=3
a=[]
for i in range (n):
    b=[]
    for i in range(n):
        b.append(int(input()))
    a.append(b)
for i in range(n):
    for j in range(n):
        print(a[i][j],end=" ")
    print()
k=0
sumn=0
for i in range(n):
    for j in range(i+1,n):
        if a[i][j]>0:
            sumn+=a[i][j]
            k+=1
print('кол-во',k,'сумма',sumn)
