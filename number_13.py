from ipaddress import *
k = 0
n = ip_network(f'174.114.120.0/255.255.252.0',0)
for x in n:
    x = f'{x:b}'
    if x.count('1')%2==0:
        k+=1
print(k)