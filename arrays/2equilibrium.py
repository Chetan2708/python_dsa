

# sum before the equilibrium point is same as the sum after the equilibrium point
def equi(l):
    #left and right sum variables
    left = 0 
    r_sum = 0 
    for i in range(0, len(l)):
        r_sum+=l[i]  #sum of all elements
    print (r_sum)
    for i in range(0, len(l)):
        r_sum-=l[i]     #removing 1st element from sum , then comparing it with the left_sum
        print (r_sum)
        if r_sum==left:  #comparing , if equal return index
            return "Equilibrium Point ", i                    
        else:                                 #incrementing if it's not equal to the right sum 
            left+=l[i]     
            print (left)              
    return -1         
     


l = [-7, 1, 5, 2, -4, 3, 0]
print(equi(l))
