def search(l ,x):
    l.sort()
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low +( high-low) // 2
        if l[mid]==x:
            return mid
        elif l[mid]>x: 
            high = mid-1
        elif l[mid] < x:
            low = mid + 1
    return -1
l = []
n = int(input("enter the number :"))
for i in range(n):
    f = int(input("enter the numbers for list :"))
    l.append(f)
x = int(input("enter the numbers you want to search for :"))
print(search(l,x))