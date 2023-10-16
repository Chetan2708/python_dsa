def lengthOfLongestSubstring(s):

    char = [-1]*256 
    length = 0 
    l = 0 
    r = 0 
    n = len(s)
    while r < n:
        if char[ord(s[r])]!= -1:
            l = max(char[ord(s[r])]+1 , l)
        char[ord(s[r])] = r 
        length = max(length , r - l +1)
        r+=1
    return length

print(lengthOfLongestSubstring("abciab"))