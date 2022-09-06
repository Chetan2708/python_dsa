def create_seperator(l):
    even =[]
    odd = []
    # for i in l:
    #     if i % 2 == 0:
    #         even.append(i)
    #     else:
    #         odd.append(i)
    # return even, odd
    l1 = [i for i in l if i % 2 == 0]
    l2=  [i for i in l if i % 2 != 0]
    return l1,l2  
l = []  
n = int(input("enter the number of observations  : "))
for i in range(n):
    t = int(input(f"Enter the number {i+1} : "))
    l.append(t)
l1,l2 = create_seperator(l)
print(l1)
print(l2)