file = open(r"C:\Users\Windows 10\Documents\Новая папка\Мохова А.Ю.-У-224-ввод1.txt",encoding='utf-8')
q = open(r"C:\Users\Windows 10\Documents\Новая папка\Мохова А.Ю.-У-224-ввод1.txt",encoding='utf-8')
file1 = open(r"C:\Users\Windows 10\Documents\Новая папка\Мохова А.Ю.-У-224-вывод1.txt", 'w+',encoding='utf-8')
w = q.readlines()
e = file.readlines(5)
r = file.readlines()
a = [int(x) for x in w]
b = [int(x) for x in e]
c = [int(x) for x in r]
def F(s,d):
    file1.write('Номера строк:')
    for i in b:
        if i == s:
            file1.write('0')
            break
    for i in c:
        if i == s:
            file1.write('1')
            break
    file1.write('\n')
    for i in a:
        if i == s:
            i *= d
            file1.write(str(i))
        else:
            file1.write(str(i))
    file1.write('\n')
F(2,3)
file1.close()
