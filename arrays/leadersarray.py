
def lead(l,n):
#     for i in range( len( l ) ) :
#         flag = False
#         for j in range( i+1 , len( l ) ) :
#             if l[j]>=l[i]:
#                 flag = True 
#                 break
#         if flag ==False :
#             l1.append(l[i])
#     return l1

    l1 = []
    max = l[n-1]
    l1.append(max)
    for i in range(n-2, -1 , -1 ):
        if  max < l[i] :
            max = l[i]
            l1.append(max)
    return l1[::-1]
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(lead(l,n))