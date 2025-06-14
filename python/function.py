def func(var1, var2):
    if var1 >= var2:
        for var2 in range(var2, var1, 1):
            if(var2%2==0):
                print(var2)
    else:
        for var1 in range(var1, var2, 1):
            if(var1%2==0):
                print(var1)

func(50, 10)