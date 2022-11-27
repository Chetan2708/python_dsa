def oddone(l):
    # res = 0 
    # for i in l:
    #     res = res ^ i    #xor of any element with 0 is always the number itself and xor of any element with itself is always zero 
    # return res            #here it will return the odd number out as all the other will be xored out
    l3=[]
    for i in l:
        l2 =l.count(i) 
        if l2 %2 != 0:
         l3.append(i)
    return l3

l = []
n = int(input())
for i in range(0, n):
    f = int(input("Enter numbers in pair or single  :"))
    l.append(f)
print(oddone(l))