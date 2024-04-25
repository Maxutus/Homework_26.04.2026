print('x y w z f')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (w<=z) and ((y<=x) == (z<=y))
                if f == 1 and x+y+w+z >= 1 and x+y+w+z<4:
                    print(x,y,w,z,int(f))