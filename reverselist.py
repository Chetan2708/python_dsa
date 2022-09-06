def rev(l):
    start = 0
    end = len(l)-1
    for i in range(start, end):
        if start<end:
            l[start] , l[end] = l[end] , l[start]    #swap
            start = start + 1
            end = end - 1
    return l
# def rev(l):  #library method
#     l2 = list(reversed(l))
#     return l2
# def rev(l):  #list slicing
#     l2 = l [ ::-1]
#     return l2
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(rev(l))