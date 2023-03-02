def search(l):
    low = 0
    high = len(l)-1
    while low<=high:
        mid = low+(high-low)//2
        if l[mid]>1:
            high = mid-1
        elif l[mid]<1:
            low=mid+1
        else:
            if l[mid]==0 or l[mid-1]!=1:
                return mid
            else:
                high=mid-1 

l=[0,0,0,1,1,1,1]
count = search(l)
print(len(l)-count)