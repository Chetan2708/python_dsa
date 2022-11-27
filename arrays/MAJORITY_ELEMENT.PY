 ##MOORE VOTING ALGORITHM
def more(l,n):
    count = 1 
    res = 0
    for i in range(1,len(l)):
        if l[res]==l[i]:
            count+=1
        else:
            count-=1
        if count == 0:
            res = i
            count = 1 
    count = 0
    for i in range(len(l)):
        if l[res] == l[i]:
            count +=1
    if count<=n/2:
        res = -1
    return res
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(more(l,n))


