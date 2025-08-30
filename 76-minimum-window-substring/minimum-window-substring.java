import java.util.*;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";

        // Step 1: Store frequency of all chars in t
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        Map<Character, Integer> window = new HashMap<>();
        int i = 0, j = 0; // i = left, j = right
        int required = need.size(); // how many distinct chars we need
        int formed = 0; // how many chars matched
        int minLen = Integer.MAX_VALUE;
        int start = 0;

        // Step 2: Expand with j
        while (j < s.length()) {
            char c = s.charAt(j);
            window.put(c, window.getOrDefault(c, 0) + 1);

            // If char count matches the need, we formed one requirement
            if (need.containsKey(c) && window.get(c).intValue() == need.get(c).intValue()) {
                formed++;
            }

            // Step 3: Try to shrink with i while window is valid
            while (i <= j && formed == required) {
                if (j - i + 1 < minLen) {
                    minLen = j - i + 1;
                    start = i;
                }

                char leftChar = s.charAt(i);
                window.put(leftChar, window.get(leftChar) - 1);
                if (need.containsKey(leftChar) && window.get(leftChar) < need.get(leftChar)) {
                    formed--;
                }
                i++;
            }

            // Move right pointer forward
            j++;
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
