def stock_check(l):
    count = 0
    res = 0 
    for i in range (len(l)):
        if l[i]==1:
            count+=1
            res = max(res,count)
        else:
            count = 0
    return res
l = []
n = int(input())
for i in range(n):
    f = int(input())
    l.append(f)
print(stock_check(l))
