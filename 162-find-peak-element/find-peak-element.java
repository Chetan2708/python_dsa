class Solution {
    public int findPeakElement(int[] nums) {
    int low = 0, high = nums.length - 1;

    while (low < high) {
        int mid = low + (high - low) / 2;

        if (nums[mid] > nums[mid + 1]) {
            high = mid;  // Peak is on the left
        } else {
            low = mid + 1;  // Peak is on the right
        }
    }

    return low;  // 'low' is the peak index

}
}