def fact(x):
    if x == 1:
        print (1)
        return 1
    else:
        # print ("doing call stack")
        # print (x * fact(x-1))
        return x * fact(x-1)
      
fact(3)