N_R = 0
mn_R = 10**10
for N in range(10000):
    R = bin(N)[2:]
    if N%3==0:
        R = R + '010'
    else:
        R = R + bin(5 * (N%3))[2:]
    R = int(R,2)
    if R > 300 and R%2==0:
        if R<=mn_R:
            mn_R = R
            N_R = N
print(N_R)