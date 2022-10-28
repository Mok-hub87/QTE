n=[3,6,9,2,32,10,8,5,67,4,0,56]
m=[]
for i in n:
    if i%2==1:
        m.append(i)
        if sum(m)==0:
            print('no such numbers')
m.sort()
m.reverse()
print(m)
