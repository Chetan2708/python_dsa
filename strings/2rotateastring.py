def check(s1,s2):
    if len(s1) != len(s2):
        return False
    temp = ''
    temp=s1+s1
    return temp.find(s2) != -1
s1= input("enter:")
s2= input("enter2:")
print(check(s1,s2))