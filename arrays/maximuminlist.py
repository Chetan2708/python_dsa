def maximum(arr, n):
    maxi = arr[0] 
    for j in range(1,n):
            if maxi<arr[j]:
                maxi = arr[j]
    return maxi
def mini(arr, n):#code here
        sm = arr[0]
        for i in range(1,n):
            if sm>arr[i]:
                sm=arr[i]
        return sm
def sumOfMaxandMin(arr, n):
        t = maximum(arr,n)
        a = mini(arr,n)    
        return t+a     

arr =[]
n = int(input())
for i in range(n):
    f = int(input())
    arr.append(f)
print(f"addition of max and min val is: {sumOfMaxandMin(arr,n)}")