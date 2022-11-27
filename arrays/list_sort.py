def sort(l):
    for i in range(1,len(l)):
        if l[i]<l[i-1]:
            return False 
    return True   
l =[]
n = int(input())
for i in range(n):
    f = int(input()) 
    l.append(f)
print(f"sorted list is: {sort(l)}")
