def check(s1):
    if len(s1) ==0:
        return False
    if s1[0:] == s1[::-1]:
        return True
    else:
        return False

s1= input("enter:")
print(check(s1))