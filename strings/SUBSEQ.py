def sub(s1,s2):
        i ,j = 0,0
        while (i < len(s1) and j < len(s2)):
            if s1[i] == s2[j]:
                j += 1
            i +=1
        if j == len(s2):
            return True
        else:
            return False

s1 = input('s1')
s2 = input('s2')
print (sub(s1, s2))
