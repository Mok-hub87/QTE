def F(variable):
    if len(variable)==1:
        return variable
    else:
        return variable[-1]+F(variable[:-1])
a=F(input())
print(a)
