def listMax(mylist):
    for i in range(len(mylist)):
        a = mylist[i]
        b = mylist[i+1]
        if a < b:
            t = b
        else:
            t = a
    print(t)


listMax([1,2,3,4])
