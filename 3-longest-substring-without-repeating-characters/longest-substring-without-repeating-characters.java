import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int n = s.length();
        int i = 0, maxLen = 0;

        for (int j = 0; j < n; j++) {
            char ch = s.charAt(j);

            // if char already seen inside window, move left pointer
            if (map.containsKey(ch) && map.get(ch) >= i) {
                i = map.get(ch) + 1;
            }

            map.put(ch, j); // update last seen index
            maxLen = Math.max(maxLen, j - i + 1);
        }

        return maxLen;
    }
}
