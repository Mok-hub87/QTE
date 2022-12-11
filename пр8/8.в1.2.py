def F(a):
    return [i for i in range (a,16)]
def F1(b):
    return [i for i in range (b,16)]
def F2(c):
    return [i for i in range (c,16)]
s1=sum(F(1))
l1=len(F(1))
m1=s1/l1
s2=sum(F1(2))
l2=len(F1(2))
m2=s2/l2
s3=sum(F(3))
l3=len(F(3))
m3=s3/l3
print('1)',s1,m1,'2)',s2,m2,'3)',s3,m3)
