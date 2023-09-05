def sort(l):
        low = 0 
        high = len(l)-1
        mid = 0 
        # code here
        while mid<=high:
            if l[mid] == 0:
                l[mid] , l[low] = l[low] ,l[mid]
                mid+=1
                low+=1
            elif l[mid] ==1:
                mid+=1
            else:
                l[mid] ,l[high] = l[high] , l[mid]
                high-=1


l=[1,0,2,0]
sort(l)
print(l)