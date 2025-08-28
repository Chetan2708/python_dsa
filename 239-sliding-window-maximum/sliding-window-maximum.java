import java.util.*;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> ans = new ArrayList<>();
        Deque<Integer> qu = new ArrayDeque<>(); // store indices instead of values
        int i = 0, j = 0;
        int n = nums.length;

        while (j < n) {
            // Remove smaller elements from back
            while (!qu.isEmpty() && nums[qu.peekLast()] < nums[j]) {
                qu.pollLast();
            }
            qu.offerLast(j);

            // Window not yet of size k
            if (j - i + 1 < k) {
                j++;
            }
            // Window hit size k
            else if (j - i + 1 == k) {
                ans.add(nums[qu.peekFirst()]);

                // Remove element going out of window
                if (qu.peekFirst() == i) {
                    qu.pollFirst();
                }
                i++;
                j++;
            }
        }
        int[] result = new int[ans.size()];
        for (int idx = 0; idx < ans.size(); idx++) {
            result[idx] = ans.get(idx);
        }

        return result;
}
}