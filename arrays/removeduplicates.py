def remove(l):
    res = 1 
    for i in range(1 , len(l)):     #copying the first element as it is .
        if l[i] != l[i-1]:                 #checking the second element with the first element , if same copy it in the original array else do nothing
            l[res]=l[i]
            res+=1                           #increment res 
    return res
l = [1,1,1,2,2,3,3,3,3,3,3,3,3,3]
res = remove(l)
for i in range(res):
    print(l[i],end="")

# dry run [  1 , 1  ,2 ,3  ]

