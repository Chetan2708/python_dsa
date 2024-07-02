class Solution:
    def reverseVowels(self, st: str) -> str:
        s = list(st)
        start = 0
        end = len(s) - 1
        vowels = set("aeiouAEIOU")
        
        while start < end:
            if s[start] not in vowels:
                start += 1
            elif s[end] not in vowels:
                end -= 1
            else:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
                
        return "".join(s)