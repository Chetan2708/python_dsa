import java.util.*;

class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        int n = s.length();

        // Step 1: Store frequency of all chars in t
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int i = 0, j = 0;
        int formed = t.length();   // total chars we still need
        int minLen = Integer.MAX_VALUE;
        int start = 0;

        while (j < n) {
            char ch = s.charAt(j);

            // if this char was still needed, reduce formed
            if (need.getOrDefault(ch, 0) > 0) {
                formed--;
            }

            // decrement count in need map
            need.put(ch, need.getOrDefault(ch, 0) - 1);

            // try shrinking from left while valid
            while (formed == 0) {
                if (minLen > j - i + 1) {
                    minLen = j - i + 1;
                    start = i;
                }

                char left = s.charAt(i);
                need.put(left, need.getOrDefault(left, 0) + 1);

                // if we removed a required char, window invalid again
                if (need.get(left) > 0) {
                    formed++;
                }
                i++;
            }

            j++;
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
