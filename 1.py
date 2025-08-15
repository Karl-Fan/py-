for i in range (1,10):
    for j in range (0,10):
        for k in range (0,10):
            a=str(i)
            b=str(j)
            c=str(k)
            d=a+b+c
            d=int(d)
            if i*i*i+j*j*j+k*k*k == d:
                print(d)
#水仙花数

