
def candsay(n):
        start = '1' #freq 1 always 
        for i in range(1,n):
            temp = ''
            freq = 1
            for j in range(len(start)):
                if j < len(start)-1 and start[j] == start[j+1]:
                    freq+=1
                else:
                    temp += str(freq) + start[j]   
                    freq =1 
                
            start = temp 

        return start 


nums = [ 1,2,3,4,5,6]
print(candsay(len(nums)))