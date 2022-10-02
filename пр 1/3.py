age=int(input())
name=input()
if age>16 or age==16 and 0<age<75:
    print('Поздравляем вы поступили в ВГУИТ')
else:
    print('Сначала нужно окончить школу',(16-age))