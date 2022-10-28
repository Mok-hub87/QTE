n=int(input())
if n<=9:
    for i in range (n+1):
        for x in range (1,i+1):
            print(x,end='')
        print()
else:
    print('...')
    