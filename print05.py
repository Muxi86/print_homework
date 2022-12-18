for i in range(4):
    for j in range(4-i):
        print(" ", end = ' ')
    for j in range(i):
        print(i, end = ' ')
    for j in range(1,i):
        print(i, end = ' ')
    print( )