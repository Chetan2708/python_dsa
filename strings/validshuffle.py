def checklength(s1 ,s2 , res):
    if len(s1)+len(s2)!= len(res):
        return False
    else:
        return True


def sort (s):
    l = [ ]
    for char in s :
        l.append(char)
    l.sort()
    l= ''.join(l)
    return l


def check (s1, s2, res):
    s1  = sort(s1)
    s2 = sort(s2)
    res = sort(res)
    i , j , k = 0 , 0 , 0 
    while k!= len(res):
        if i < len(s1) and s1[i]== res[k]:
            i+=1
        elif j < len(s2) and s2[j]== res[k]:
            j+=1

        else:
            return False
        k+=1

    if(i <len(s1) or j < len(s2)) :
      return False
    return True


first = "XY"
second = "12"
results = ["1XY2", "Y1X2", "Y21XX"]

for result in results:
    if checklength(first, second, result) and check(first, second, result):
        print(result + " is a valid shuffle of " + first + " and " + second)
    else:
        print(result + " is not a valid shuffle of " + first + " and " + second)


#Steps
#Sort the strings 
#check characters one by one using two pointers on each string and also on a result string 
#check combined lengths of both strings because if s1 +s2 != res then it will not be a valid shuffle 
