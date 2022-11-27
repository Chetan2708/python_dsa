def mean_avg(l):
    print(l)
    sum = 0
    for i in l:
        sum = sum + i
    return sum/f 

l = []
n = int(input("enter the number of observations"))
for a in range(0,n):
    abc = int(input("enter the valyues"))
    l.append(abc)
f = len(l)
print(f"mean of the given list is {mean_avg(l)}")