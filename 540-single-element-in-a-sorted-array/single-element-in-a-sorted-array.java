class Solution {
    public int singleNonDuplicate(int[] nums) {
    int low = 0, high = nums.length - 1;

    while (low < high) {
    int mid = low + (high - low) / 2;

    // If mid is even, its duplicate should be at mid + 1; if odd, at mid - 1.
    if (nums[mid] == nums[mid ^ 1]) {
        low = mid + 1;
    } else {
        high = mid;
    }
    }

return nums[low];
}
}