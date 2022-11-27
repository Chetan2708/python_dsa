#check for anagram using hashmaps
import re


def check_for_anagram(s , t):
    if len(s)!=len(t):
        return False
    Hm ,Hm1 ={},{}
    for i in range(len(s)):
        Hm[s[i]]=1+Hm.get(s[i], 0)
        Hm1[t[i]]=1+Hm1.get(t[i],0)

    for i in Hm:
        if Hm[i]!=Hm1.get(i,0):
            return False
        else:
            return  True
         
s=input()
t=input()
print(check_for_anagram(s,t))    