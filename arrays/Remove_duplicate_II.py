def fun (l):    
    count = 1 
    res = 1
    for i in range(1, len(l)):
        if l[i] == l[i-1]:
            count+=1
        else:
            count =1
        if count<=2:
            l[res] =l[i]
            res+=1 
    return res


l = [1,1,1,2,2,3,3,3,3,3,3,3,3,3]
res = fun(l)
for i in range(res):
    print(l[i],end="")