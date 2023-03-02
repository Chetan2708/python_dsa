def rev(n):
    if n == 0 :
        return 
    re= n%10
    print(re , end ="")
    return rev(n//10) 
rev(12)