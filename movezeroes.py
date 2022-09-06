def mov(l):
    count = 0
    for i in range(len(l)):
        if l[i] != 0:
            l[i] ,l[count] =  l[count], l[i]
            count += 1
    return l 
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(mov(l))

     