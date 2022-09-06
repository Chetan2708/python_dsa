def sub(l,sum1):
    curr = 0
    start = 0
    a=[]
    for i in range(len(l)):
        curr += l[i]
        while (curr>sum1) :
            curr -= l[start]
            start+=1
        if (curr == sum1): 
            return True
    if sum==0 or len(a)==0:
        return -1
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
sum1 = int(input())
print(sub(l,sum1))