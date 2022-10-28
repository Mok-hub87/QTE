n=int(input())
def F(n):
    return sum(i*i*i for i in range(n+1))
print(F(n))
