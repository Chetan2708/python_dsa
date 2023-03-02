# def fun(l):
#     for i in range(len(l)):
#         if l[i]==x:
#             return(i)
#     return -1
def fun(l):
    low =0
    high = len(l) - 1  
    index =-1        #[5,10,10,20,20]    
    while low <= high:
        mid = low+(high-low)//2
        print(mid)
        if l[mid]==x:
            index=mid
            high=mid-1
        if x>l[mid]:
            low=mid+1
        elif x<l[mid]:
            high = mid -1
    return index

             
#sorted array
l= [5,10,10,10,20,20]
x=10
print(fun(l))
