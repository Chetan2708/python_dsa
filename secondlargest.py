# def lrge(arr):
#     max = 0
#     for i in range(0, len(arr)): 
#         if arr[i]>max:
#             max = arr[i]
#     return max
# def scndlrge(arr):
#     scnd = 0 
#     lar = lrge(arr)
#     for i in arr[0:]:
#         if i != lar:
#             if scnd ==None:
#                 scnd = i 
#             else:
#                  scnd =max(scnd , i)
#     return scnd
# arr =[]
# n = int(input())
# for i in range(n):
#     f = int(input())
#     arr.append(f)
# print(f"scndmax val is: {scndlrge(arr)}")


def scndlrge(arr):
    lar = arr[0]
    scl= None
    for x in arr[1:]:
        if x> lar:
            scl = lar 
            lar = x
        elif x != lar:
            if scl ==None or scl<x:
                scl =x
    return scl

arr =[]
n = int(input())
for i in range(n):
    f = int(input())
    arr.append(f)
print(f"scndmax val is: {scndlrge(arr)}")

