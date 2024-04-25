def f(a,b,p):
    if a+b>=80 and p == 3:
        return True
    if a+b>=80 and p == 2:
        return False
    if a+b<80 and p == 3:
        return False
    if p%2 == 0:
        return f(a+1,b,p+1) or f(a,b+1,p+1) or f(a+b,b,p+1) or f(a,a+b,p+1)
    if p%2 == 1:
        return f(a+1,b,p+1) or f(a,b+1,p+1) or f(a+b,b,p+1) or f(a,a+b,p+1)
for S in range(1,72):
    if f(8,S,1):
        print(S)
        break