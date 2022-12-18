for i in range(5):
    for j in range(4-i):
        print(" ", end = ' ')
    for j in range(i):
        print("*", end = ' ')
    for j in range(1,i):
        print("*", end = ' ')
    print( )