def fun(nums):
      

    # using hashmap
    Dict = {i:0 for i in l}

    for i in range(len(l)):
        if (Dict[l[i]] == 0):
            print(l[i],end=" " )
            Dict[l[i]] = 1   #TO SHOW THAT THE PARTICULAR ELEMENT IS ENCOUTERED BEFORE 


    #USING SET 
    # unique_set  = set()

    # for i in range(len(l)):
    #     unique_set.add(l[i])
    
    # print(list(unique_set))


l = [1, 2, 5,  7, 2, 4, 2]
print(fun(l))