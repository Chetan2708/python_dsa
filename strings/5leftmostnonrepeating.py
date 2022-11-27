import sys
CHAR =256
def nonrep(s):
    fi = [-1]*CHAR
    for i in range(0, len(s)):
        if fi[ord(s[i])] ==-1:
            fi[ord(s[i])] = i
        else:
            fi[ord(s[i])] = -2
    res = sys.maxsize
    for i in range(0, len(s)):
        if fi[ord(s[i])]>0:
            res = min(res, fi[ord(s[i])])
    return res
s1= input("Enter tHE String:- ")
print(nonrep(s1))