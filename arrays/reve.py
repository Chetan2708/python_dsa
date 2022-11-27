def fac(n):
    if n == 0 or n == 1:
        return 1 
    fac = 1
    for i in range(1,n+1):
        fac = fac * i 
    return fac







n = int(input("Enter the number: "))
print(fac(n))
# count = n
# while True:
#     x =str(n)
#     y = x[::-1]
#     if x==y:
#         print(x, "is palindrome , when the number is", count)
#         break
#     n = int(x)+int(y)

