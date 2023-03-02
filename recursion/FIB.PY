def fun(n):
    if n<=1:
        return n
    return fun(n-1)+fun(n-2)
    # a = 0
    # b = 1
    # if n < 0:
    #     print("Incorrect input")
    # elif n == 0:
    #     return a
    # elif n == 1:
    #     return b
    # else:
    #     for i in range(2,n+1):
    #         c = a + b
    #         a = b
    #         b = c
    #     return b
print(fun(14))