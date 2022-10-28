seconds=int(input())
day=seconds//86400
hour=seconds//3600//9
minute=seconds%3600//60
seconds=seconds%86400
seconds=seconds%60
print(day,hour,minute,seconds)