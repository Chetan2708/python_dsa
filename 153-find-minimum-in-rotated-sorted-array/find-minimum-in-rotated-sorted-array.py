class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            return nums[0]

        middle_index = len(nums) // 2
        middle_number = nums[middle_index]
        last_number = nums[-1]

        if middle_number > last_number:
            return self.findMin(nums[middle_index:])
        else:
            return self.findMin(nums[:middle_index + 1])