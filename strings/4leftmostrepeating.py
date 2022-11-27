import sys
CHAR =256
def rep(s):
    # res = sys.maxsize                                 #O(n)
    # fi = [-1]*256
    # for i in range(len(s)):
    #     if fi[ord(s[i])] == -1:
    #         fi[ord(s[i])] = i
    #     else:
    #         res = min(res, fi[ord(s[i])])
    # if res == sys.maxsize:
    #     return -1
    # else:
    #     return res
    res = -1                                              #O(n)................. better than previous because it does less comparisons
    fi = [False]*CHAR
    for i in range(len(s)-1 , -1 , -1):
        if fi[ord(s[i])]== False:
            fi[ord(s[i])] = True
        else:
            res = i 
    return res
s1= input("Enter:")
print(rep(s1))