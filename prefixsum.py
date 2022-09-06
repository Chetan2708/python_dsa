def prefix(l,n):
    prefix_sum[0]=l[0]
    for i in range( 1, len(l) ):
        prefix_sum[i]= prefix_sum[i-1] +l[i]

def getsum(prefix_sum, le , r):
    if le != 0 :
        return prefix_sum[r]-prefix_sum[le-1]
    else:
        return prefix_sum[r]
l = []
n= int(input(""))
for i in range (n):
    f = int(input(" "))
    l.append(f)
le = int(input(" "))
r = int(input(" "))
prefix_sum =n*[0]
prefix(l,n)
print(getsum(prefix_sum,le, r))