def first(x):
    low = 0
    high = len(l)-1
    index=-1
    while low <= high:
        mid = low +(high-low)// 2 #int has limit , it will overflow if (low +high / 2)
        if l[mid]==x:
            index=mid
            high =mid-1
        elif l[mid]>x: 
            high = mid-1
        elif l[mid] < x:
            low = mid + 1
    return index
def last(x):
    low = 0
    high = len(l)-1
    index2=-1
    while low <= high:
        mid = low +(high-low)// 2 #int has limit , it will overflow if (low +high / 2)
        if l[mid]==x:
            index2=mid
            low=mid+1
        elif l[mid]>x: 
            high = mid-1
        elif l[mid] < x:
            low = mid + 1
    return index2
l=[1,10,10,20,30,40,40,40,40,40]
x=first(40)
y=last(40)
print((y-x)+1)

