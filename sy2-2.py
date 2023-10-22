for b in range(0, 100):
    for m in range(0, 100):
        for s in range(0, 100):
            if (5*b+3*m+s/3)==100 and b+m+s==100:
                print(b, m, s)