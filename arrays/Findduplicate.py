 
# Linked list method to find duplicate using slow and fast pointers  FLoyds cycle detection , O(n) time and O(1) space


def find(l):
    slow , fast = l[0] , l[0]
    while True :
        slow = l[slow]
        fast = l[l[fast]]
        print('slow',slow , fast )
        if  (slow == fast ):
            break
    start = l[0]
    while start != slow:
        start = l[start]
        slow = l[slow]
    return slow




l = [1,2,3,4,5,7,3,6,9]
print(find(l))
