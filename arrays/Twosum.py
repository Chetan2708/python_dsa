def fun(l,target):
#  #Brute force
#     for i in range(len(l)):
#         for j in range(i+1, len(l)):
#             if l[i]+l[j]==target:
#                 return [i , j ]

#Hashmap used 
# Return index of the elements that are added up and gives output == target    

    # hsh = {}
    # for i, n in enumerate(l):
    #     difference = target - n 
    #     if difference in hsh:     #if element found e.g 9-7 =2 , its present in hashmap , return 7's index and 2's index 
    #         return [hsh[difference] , i]      
    #     hsh[n] = i          #Basically maintaining hashmap with each value and its index 
        
#Two pointer approach 

    l.sort()
    print(l)
    for i in range(len(l)):
        left=0
        right=len(l)-1
        
        while (left<right):
            if l[left]+l[right]==target:
                return [l[left] ,l[right]]
            elif l[left]+l[right]> target:
                right-=1
            else:
                left+=1

    return False


l = [3,2,4]
target = 6 
print(fun(l,target))