class Solution {

    // Never forget if search in sorted  array then first check the left half array then the right half
    // Which so ever is sorted check if the target value lies in them  just get that one and start working with that 

    public int search(int[] nums, int target) {

        // First do binary search
        int low= 0  , high = nums.length - 1 ;
        while( low <= high ){
            int mid = low + (high -low) /2 ;

            if (nums[mid] == target ) {
                return mid;
            }

            if (nums[mid] >= nums[low]){ //left sorted
                    if(target >= nums[low] && target < nums[mid]) high = mid -1 ; //Target Lies In between
                    else low = mid +1 ; // Target is not in between go for right
            }
            else {
                if(target > nums[mid] && target <= nums[high]) low = mid +1 ; //Target Lies In between
                else high = mid -1 ; // Target is not in between go for right
            }
        }

        return -1 ;
        
    }
}