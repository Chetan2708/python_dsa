
def fun(l):
    low =0
    high = len(l) - 1
    index = -1          #[5,10,10,20,20]    
    while low <= high:
        mid = low+(high-low)//2
        if l[mid]==x:
            index =mid 
            low=mid+1
        if x>l[mid]:
            low=mid+1
        elif x<l[mid]:
            high = mid -1
    return index
l= [5,10,10,20,20]
x=20
print( fun(l) )
