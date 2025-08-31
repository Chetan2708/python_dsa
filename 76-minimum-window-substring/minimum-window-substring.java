import java.util.*;

public class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        int n = s.length();

        // Step 1: Store frequency of all chars in t
        Map<Character, Integer> need = new HashMap<>();
        for (char c : t.toCharArray()) {
            need.put(c, need.getOrDefault(c, 0) + 1);
        }

        int i = 0, j = 0;
        int count = 0;   // how many chars we matched
        int minLen = Integer.MAX_VALUE;
        int start = 0;

        while (j < n) {
            char ch = s.charAt(j);

            // if this char is still needed, increase count
            if (need.getOrDefault(ch, 0) > 0) {
                count++;
            }

            // decrement count in need map (even if not needed, we track surplus)
            need.put(ch, need.getOrDefault(ch, 0) - 1);

            // try shrinking from left while valid
            while (count == t.length()) {
                if (minLen > j - i + 1) {
                    minLen = j - i + 1;
                    start = i;
                }

                char left = s.charAt(i);
                need.put(left, need.getOrDefault(left, 0) + 1);

                // if removing left breaks requirement, reduce count
                if (need.get(left) > 0) {
                    count--;
                }
                i++;
            }

            j++;
        }

        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}