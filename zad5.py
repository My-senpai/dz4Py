# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.



def getElementList(st):
    st = st.replace('-','+-')

    if st[0] == '+':
        st = st.replace('+','',1)
    ls = st.split('=')
    ls = ls[0].replace(' ','')
    ls = ls.split('+')
    return ls

def getStepNumber(st):
    if 'x^' in st:
        i = st.find('^')
        n = int(st[i+1:])
    elif ('x' in st) and ('^' not in st):
        n = 1
    else:
        n = 0
    return n

def getCoefficient(st):
    if 'x' in st:
        i = st.find('x')
        n = int(st[:i-1])
    else:
        n = int(st)
    return n

def getCoefficientList(lst):
    l = []
    k = getStepNumber(lst[0])
    i = 0
    j = 0

    while i <= k:
        if getStepNumber(lst[j]) != k-i:
            l.append(0)
        else:
            l.append(getCoefficient(lst[j]))
            j += 1
        i += 1
    return l

file1 = open('file1.txt', 'r')
str1 = file1.read()
file1.close()
file2 = open('file2.txt', 'r')
str2 = file2.read()
file2.close()
rep = open('file3.txt', 'w')

lst1 = getElementList(str1)
lst2 = getElementList(str2)
kl1 = getCoefficientList(lst1)
kl2 = getCoefficientList(lst2)

while len(kl1) != len(kl2):
    if len(kl1) > len(kl2):
        kl2.insert(0,0)
    else:
        kl1.insert(0,0)

resSt = ''

for i in range(len(kl1)):
    if len(kl1)-1-i > 1:
        resSt = resSt + str(kl1[i]+kl2[i]) + 'x^' + str(len(kl1)-1-i) + '+'
    elif len(kl1)-1-i == 1:
        resSt = resSt + str(kl1[i]+kl2[i]) + 'x' + '+'
    else:
        resSt = resSt + str(kl1[i]+kl2[i])

resSt = resSt.replace('+-','-')
resSt = resSt + '=0'
rep.writelines(resSt)
rep.close()