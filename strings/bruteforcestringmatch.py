
def match(s1,s2):
    n=len(s1)
    m = len(s2)
    for  i in range(n-m+1):
        j=0
        while j <m:
            if s2[j] != s1[i+j]:
                break
            j=j+1
        if j == m:
            print(i, end = " ")
    else:
        return -1




s1 = input()
s2 = input()
match(s1,s2)   