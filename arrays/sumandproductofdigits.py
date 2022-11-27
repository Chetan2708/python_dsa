def sumOfProductOfDigits(n1, n2):
    #your code here
    sum = 0
    while (n1 and n2 !=0):
        pr1 = n1%10
        pr2 = n2%10
        sum += pr1*pr2
        n1=n1//10
        n2=n2//10
    return sum

n1 = int(input(""))
n2 = int(input(""))
print (sumOfProductOfDigits(n1, n2))