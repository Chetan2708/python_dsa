def subar(l):
    curr_sum = 0 
    maX_sum = l[0]
    for i in range(len(l)):
        curr_sum += l[i]
        if curr_sum > maX_sum:
            maX_sum = curr_sum
        if curr_sum <0:
            curr_sum = 0
    return maX_sum

l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)  
print(subar(l))