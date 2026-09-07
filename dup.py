def dup(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    return a
print(dup([1,2,3,1,4,5,7,8,9,4,5]))
