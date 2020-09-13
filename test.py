s = open('input.txt','r')
a = []
for i in s:
    a.append(list(i.split(':')))
b = []
for i in a:
    b.append(i[-1].replace('\n',''))
for i in range(len(a)):
    a[i][-1] = b[i]
n = a.pop(-1)
num = int(n[0])
a.sort()
str = ''
for i in a:
    if num % int(i[0]) == 0:
        str += i[1]
if str == '':
    print(num)
else:
    print(str)
