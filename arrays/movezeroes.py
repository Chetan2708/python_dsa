def mov(l):
    count = 0
    for i in range(len(l)):
        if l[i] != 0:                #non zero elemnt 
            l[i] ,l[count] =  l[count], l[i] #swap non zero element after zero to before zero index (count is holding the index where the first zero started)
            count += 1
    return l  
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(mov(l))

     