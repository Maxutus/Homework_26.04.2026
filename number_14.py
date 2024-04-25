def third(n):
    s = ''
    while n>0:
        s = s + str(n%3)
        n //= 3
    return s
s = 2 * 9**10 - 3**5 + 5
print(third(s).count('2'))