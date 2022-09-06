def check(l,k):
    new=[i for i in l if i < k]
    return new
l = []
n = int(input())
for i in range(n):
    f = int(input())
    l.append(f)
k = int(input("Enter the number: "))
print(check(l,k))
