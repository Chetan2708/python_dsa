
def ins(l , pos , x ,n):
    for i in range(n-1, pos-2 , -1):            # 6 ka array(1 none) ,-2 se array start krenge ,  3 is position 
        l[i+1] = l[i]                           #3 - 2 = 1   =2 position tak loop chalegi  1is not included
    l[pos] = x
    return l
                                              #[12, 3 ,4, 6, 8 , None]  , 8 copied to none , 6 to 8
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
pos = int(input("enter the position of the observation"))
x = int(input("enter the x "))
l.append(None)
print(ins(l , pos , x ,n ))