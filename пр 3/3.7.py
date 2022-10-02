q=int(input())
if q%4==0 or q%400==0 and q%100!=0:
    print("yes")
else:
    print("no")
