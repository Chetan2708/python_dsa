import java.util.*;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> charCountMap = new HashMap<>();
        int n = s.length();
        int i = 0, maxx = 0 ,j = 0 ;
        while (j < n){
            char c = s.charAt(j);
            charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);
            if (charCountMap.size() == j - i + 1) {
                maxx = Math.max(maxx, j - i + 1);
                j++;
            }
            else if(j-i+1 > charCountMap.size()) {
                while (j-i+1 >charCountMap.size() ) {
                    char leftChar = s.charAt(i);
                    charCountMap.put(leftChar, charCountMap.get(leftChar) - 1);
                    if (charCountMap.get(leftChar) == 0) {
                        charCountMap.remove(leftChar);
                    }
                    i++;
                }
                j++;
            }
        }
        return maxx;
    }
}
