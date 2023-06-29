#maximum subaray in a list
def subar(l):
    curr_sum = 0 
    maX_sum = l[0]
    for i in range(len(l)):
        curr_sum = max(curr_sum+l[i], l[i])
        maX_sum = max(maX_sum , curr_sum)
    return maX_sum 



#2nd approach (long way) 

    # def maxSubArray(self, l: List[int]) -> int:
    #     cur_sum= 0
    #     max_sum= l[0]
    #     for i in range(len(l)):
    #         cur_sum += l[i]
    #         if cur_sum>max_sum:
    #             max_sum = cur_sum
    #         if cur_sum<0:
    #             cur_sum=0
    #     return max_sum


l = []
n = int(input())
for i in range(0, n):
    f = int(input())
    l.append(f)  
print(subar(l))
