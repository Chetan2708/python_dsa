def cal_ana(string,k):
    Hm ={}
    for char in string:               
        if Hm[char] in Hm:
            Hm[char] +=1
        else: 
            Hm[char] = 1
    chars=[]
    for char in Hm:
        if Hm[char]==k:
            chars.append(char)
    return chars

x = "anagra"
k = 2
print(cal_ana(x, k))