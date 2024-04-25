s = open('24-j6.txt').readline().strip()
k = 1
mx = 0
for i in range(len(s)-1):
    if s[i+1] > s[i]:
        k+=1
    else:
        if k == 5:
            mx+=1
        k = 1
print(mx)