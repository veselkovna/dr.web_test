def fibb(n):
    a,b = 0,1
    i = 1
    DataList = [0]
    while i < n:
        a, b =b, a + b
        print(a)
        if a % 2 == 0:
            DataList = DataList + [a]
            if len(DataList) == n:
                break
    DataSTR = [str(a) for a in DataList]
    print(", ".join(DataSTR))   
fibb(10)
