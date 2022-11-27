def rev(A):
 
    last = A[-1]
    for i in reversed(range(len(A) - 1)):
        A[i + 1] = A[i]
 
    A[0] = last
    return A
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(rev(l))
