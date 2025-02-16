class Solution {
    public int findMin(int[] nums) {
        //go for the sorted part first , pick the lowest from there and you get the minimum 
        // then find in the rotated part
        int low = 0 , high = nums.length - 1 ;
        int ans = Integer.MAX_VALUE ;
        while(low <=high){
            int mid = low + (high-low) /2;

            if(nums[low] <= nums[high]){ // Already sorted Array
                ans = Math.min(nums[low], ans);
                return ans ;
            }
            if(nums[low] <= nums[mid]){ //left half sorted
                ans = Math.min(nums[low], ans); //Keep Minimum
                low = mid +1 ; //Eliminate left half
            }
            else{
                ans = Math.min(nums[mid], ans); //keep minimum from right half
                high= mid -1 ; //Eliminate right half
            }

        } 
        return ans;
    }
}