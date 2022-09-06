def maxx(arr):
    max = arr[0]
    for i in range(1, len(arr)): 
        if arr[i]>max:
            max = arr[i]
    return max
arr =[]
n = int(input())
for i in range(n):
    f = int(input())
    arr.append(f)
print(f"max val is: {maxx(arr)}")