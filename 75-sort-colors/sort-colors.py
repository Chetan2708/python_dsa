class Solution:
    def sortColors(self, l: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low , mid , high = 0 , 0  ,len(l)-1

        while mid <= high:
            if l[mid]==0:
                l[low] , l[mid] = l[mid] , l[low]
                low+=1
                mid+=1

            elif l[mid]==1 :
                mid+=1
            
            else:
                l[high] , l[mid] = l[mid] , l[high]
                high-=1

