s=input('')
q=0
w=0
for i in s:
    if i=='н':
        w+=1
    else:
        if q<w:
            q=w
        w=0
s=s.replace('!','.')
print(q)
print(s)
