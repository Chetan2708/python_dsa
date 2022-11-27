def merge(l1,l2,l3):
    i =0
    j =0
    k =0
    while i<len(l1)and j<len(l2):
        if l1[i]<l2[j]:
            temp = l1[i]
            l1[i] = l3[k]
            l3[k] = temp
            k+=1
            i+=1
        else:
            temp = l2[j]
            l2[j] = l3[k]
            l3[k] = temp
            k+=1
            j+=1

           
    while i<len(l1):
        l3[k]=l1[i]
        k+=1
        i+=1
    while j<len(l2):
        l3[k]=l2[j]
        k+=1
        j+=1
    return l3
l1= [1,3,4]
l2 =[2,5,6]
l3=[]

print(merge(l1,l2,l3))