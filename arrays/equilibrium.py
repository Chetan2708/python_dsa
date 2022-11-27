# sum before the equilibrium point is same as the sum after the equilibrium point
def equi(l):

    left_sum = 0
    sum = 0
    for i in range(len(l)):  # calculate sum of all elements
        sum += l[i]
        right_sum = sum
    for i in range(0, len(l)):
        # subtarct the fist element from sum , suppose 21 - 3 = 19
        right_sum -= l[i]
        if (left_sum == right_sum):  # compare left element to right element 0 == 19
            return 'index is', i
        left_sum += l[i]
        # add 1st element to left element 3 , now right sum = 19 ....compare it until right sum is equal to left sum
    else:
      return -1 

l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)
print(equi(l))
