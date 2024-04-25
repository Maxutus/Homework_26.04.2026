s = open('17-4.txt').readlines()
s = [int(x) for x in s]
sr = sum(s) / len(s)
mx = -10 ** 10
k = 0
for i in range(len(s) - 1):
    if s[i] < sr and s[i + 1] < sr and (s[i]%10==9 or s[i+1]%10==9):
        k+=1
        mx = max(mx,s[i]+s[i+1])
print(k,mx)
