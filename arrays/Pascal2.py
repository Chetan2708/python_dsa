def fun(n):


    #Return nth value , using optimised space

    
    res = [1]
    for i in range(1,n+1):
        res.append(1)
        for j in range(len(res)-2 , 0 , -1):
            res[j]+=res[j-1]
    return res

n = 3
temp = fun(n)   
print(temp)
