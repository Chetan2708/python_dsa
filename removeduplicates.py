def remove(l):
    res = 1
    for i in range(1, len(l)):
        if l[i]!= l[res-1]:
            l[res] = l [i]
            res+=1
    return res
def rem(l):
    n =remove(l)
    for i in range(n):
        print(l[i], end = "")
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
rem(l)