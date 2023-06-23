def fun (n):


    res = []
    for i in range(n+1):
        temp = [1 for i in range(i+1)]
        for j in range(1,len(temp)-1):
            temp[j] = res[i-1][j]  + res[i-1][j-1]
        res.append(temp)
    return res
    # res = []
    # for i in range(n):
    #     temp =[]
    #     for j in range (i+1):
    #             if j==0 or j==i:
    #                 temp.append(1)
    #             else:
    #                 temp.append(res[i-1][j-1] + res[i-1][j])
    #     res.append(temp)
    # return res 




def pattern(n,temp):
    for i in range(n):
        for j in range(n-i+1):
            print(format(" ","<2"),end="")
        for j in range(i+1):
            print(format(temp[i][j],"<4"), end="")
        print()
n = 6 
temp = fun(n)   
print(temp)
pattern(n,temp)