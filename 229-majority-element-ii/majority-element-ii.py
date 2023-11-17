class Solution:
   def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        candid1, candid2, count1, count2 = 0, 1, 0, 0
        
        for num in nums:
            if num == candid1:
                count1 += 1
            elif num == candid2:
                count2 += 1
            elif count1 == 0:
                candid1, count1 = num, 1
            elif count2 == 0:
                candid2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [num for num in (candid1, candid2) if nums.count(num) > len(nums) // 3]
