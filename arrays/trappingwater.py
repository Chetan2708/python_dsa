def trap(l, n):
    res =0
    rmax = n*[0]
    lmax = n*[0]
    lmax[0] = l[0]
    for i in range(1, len(l)):
        lmax[i] = max(l[i], lmax[i-1])
    rmax[n-1] =l[n-1] 
    for i in range(n-2 ,-1,-1):
        rmax[i] = max(l[i], rmax[i+1])
    for i in range(0, n):
        res = res + (min(rmax[i], lmax[i]) - l[i])
    return res

l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(trap(l,n))
