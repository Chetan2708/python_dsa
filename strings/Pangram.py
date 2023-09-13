# l = []
# for i in range(26):
#     l.append(False)


# def check(str):
#     str = str.lower()
#     for char in str:
#         if char != " " and char >='a'  and char<='z':
#             if l[ord(char)-ord('a')] == False:
#                 l[ord(char)-ord('a')] = True
                
# check('hi')
# flag = True
# for i in range(len(l)):
#     if l[i] ==False:
#         flag = False
#         break
# if flag :
#     print("Pangram")
# else:
#     print("Not a Pangram")

          
import string
 
alphabet = set(string.ascii_lowercase)
print(alphabet)
def ispangram(str):
     print(set(str))
     return not set(alphabet) - set(str)  #if 0 means it is a pangram because it has all alphabet characters, so not because it will give 0 as output so to invert it and return True

# Driver code
string = 'thequickbrownfox jumpsoverthelazydog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")