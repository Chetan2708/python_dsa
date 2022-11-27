def sub(l,k):
    cur = 0
    i = 0 
    for i in range(k):
        cur = cur + l[i]    
    res = cur
    for i in range(k, len(l)):
        cur = cur + l[i] - l[i - k]
        res = max(res, cur)
    return res
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
k= int(input())
print(sub(l,k))