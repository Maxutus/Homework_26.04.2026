s = open('9-183.csv').readlines()
s = [list(map(int, x.split(';'))) for x in s]
k = 0
for x in s:
    p = sum(x)/2
    S = (p * (p-x[0]) * (p-x[1]) * (p-x[2]))**0.5
    try:
        if S == int(S) and S!=0:
            k+=1
    except:
        pass
print(k)