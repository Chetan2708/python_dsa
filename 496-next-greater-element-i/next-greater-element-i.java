class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {

            Map<Integer, Integer> nextGreaterMap = buildNextGreaterMap(nums2);

            int[] ans = new int[nums1.length];
            for (int i = 0; i < nums1.length; i++) {
                ans[i] = nextGreaterMap.get(nums1[i]);
            }

            return ans;
        }

        private Map<Integer, Integer> buildNextGreaterMap(int[] nums) {

            Map<Integer, Integer> map = new HashMap<>();
            Deque<Integer> stack = new ArrayDeque<>();

            for (int i = nums.length - 1; i >= 0; i--) {

                while (!stack.isEmpty() && stack.peek() <= nums[i]) {
                    stack.pop();
                }

                map.put(nums[i], stack.isEmpty() ? -1 : stack.peek());

                stack.push(nums[i]);
            }

            return map;
        }
}