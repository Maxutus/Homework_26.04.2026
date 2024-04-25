from itertools import *
k = 0
p = product('0123456789abc', repeat= 5)
chet = [i+j for i in '02468ac' for j in '02468ac']
nechet = [i+j for i in '13579b' for j in '13579b']
for x in p:
    x = ''.join(x)
    if x.count('2') == 1 and all(i not in x for i in chet) and all(j not in x for j in nechet) and x[0]!='0':
        k+=1
print(k)