def fun(x):
    # i=1
    # while i*i <=x: 
    #     i+=1
    # return i-1
    l = 1
    high = x
    ans=-1
    while l <= high:
        mid = (l+high)// 2
        ms = mid*mid
        if ms == x:
            return mid
        elif ms > x:
            high = mid-1
        else:
            l = mid+1
            ans = mid
    return ans
x = int(input())
print(fun(x))
