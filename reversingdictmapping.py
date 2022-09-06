def rever(d1):
     d1 = {v:f for (f,v) in d1.items()}
d1={}
n = int(input())
for i in range(n):
    f = int(input())
    v = input("enter : ")
    d1[f]=v
print (d1)
print(rever(d1))