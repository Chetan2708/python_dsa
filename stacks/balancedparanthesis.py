def isMatch(a,b):
    if (a=="(" and b==")") or (a=="{"and b =="}") or  (a=="["and b=="]"):
        return True
    else:
        return False
def fun (string):
    stack=[]
    for x in string:
        if x in ("(","[","{"):         #stack has these three
            stack.append(x)
        else:
            if not stack:             #)() suppose this case stack is empty because start of the string is )
                return False
            elif isMatch(stack[-1],x)==False:
                return False
            else:
                stack.pop()             #remove one bracket from  stack if matching is Found  
    
    if stack:                        #if after the loop there is still any opening bracket left return false
        return False
    else:
        return True         #else True

string=input()
print(fun(string))
