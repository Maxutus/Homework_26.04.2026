def f(a,b,s):
    if a==b:
        return s
    if a>b:
        return ''
    if a<b:
        return f'{f(a*2,b,s+"a")} {f(a+3,b,s+"b")}'

k = 0
s = f(2,38,'').split()
for x in s:
    if 'aba' in x:
        k+=1
print(k)