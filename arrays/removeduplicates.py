def remove(l):
    res = 1 
    for i in range(1 , len(l)):
        if l[i] != l[res-1]:                 
            l[res]=l[i]                      #moving the element to the place back  , where it is not duplicate with the previous one 
            res+=1                          #incremented if element is not duplicate
    return res                             #storing how many times we removed the element 

def rem(l):
    n = remove(l)
    for i in range(n):
        print( l[i] , end = ' ')
l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
rem(l)


#dry run [  1 , 1 , 1 ,2 ]
