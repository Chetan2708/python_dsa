def peak(l):
    low =0
    high = len(l) - 1         
    while low <= high:
        mid = low+(high-low)//2
        if (mid==0 or l[mid]>l[mid-1]) and (mid== len(l)-1 or l[mid]>l[mid+1]):
            return mid
        elif mid>0 and l[mid]>l[mid-1]:
            low=mid+1
        else:
            high =mid-1
    return -1

l=[1, 3, 20, 4, 1, 0]
print(peak(l))

