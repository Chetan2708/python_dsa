class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        num_zeros = 0 
        maxx = 0 

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros +=1
            while num_zeros > k:
                if nums[l]== 0 :
                    num_zeros -= 1
                l+=1
            w = r-l+1
            maxx = max(maxx, w)
        return maxx

        