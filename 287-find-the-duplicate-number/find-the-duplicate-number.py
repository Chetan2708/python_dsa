class Solution:
    def findDuplicate(self, arr: List[int]) -> int:

        for i in range(len(arr)):
        # Mark the element at the current index as negative to indicate it has been visited
            if arr[abs(arr[i])] >= 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
            # If the element at the current index is already negative, it means it's a duplicate
                return abs(arr[i])
