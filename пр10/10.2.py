file1 = open(r"C:\Users\Windows 10\Documents\Новая папка\Мохова А.Ю.-У-224-ввод2.txt",encoding='utf-8')
file2 = open(r"C:\Users\Windows 10\Documents\Новая папка\Мохова А.Ю.-У-224-вывод2.txt", 'w+',encoding='utf-8')
R = file1.readlines()
T = file1.readlines(7)
M = file1.readlines(5)
P = file1.readlines(5)
def F(e,a,b,z):
    M = []
    for i in a:
        if i % 2 == 1:
            s = sum(a)
            M.append(s)
    for i in b:
        if i % 2 == 1:
            s = sum(b)
            M.append(s)
    for i in z:
        if i % 2 == 1:
            s = sum(z)
            M.append(s)
    for y in range(3):
        if sum(a) == max(M):
            file2.write('0')
            break
        if sum(b) == max(M):
            file2.write('1')
            break
        if sum(z) == max(M):
            file2.write('2')
            break
    file2.write('\n')
    file2.write(str(max(M)))
    F(([int(x) for x in R]),([int(x) for x in T]),([int(x) for x in M]),([int(x) for x in P]))
file2.close()
