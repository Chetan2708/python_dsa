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


def get_second_largest(arr):
    largest = arr[0]
    second_largest = None

    # Iterate over the array starting from the second element
    for x in arr[1:]:
        if x > largest:
            # If the current element is larger than the largest,
            # update the second_largest and largest accordingly
            second_largest = largest
            largest = x
        elif x != largest:
            # If the current element is not equal to the largest,
            # and it's either the first occurrence or larger than the second_largest,
            # update the second_largest accordingly
            if second_largest is None or x > second_largest:
                second_largest = x

    return second_largest

arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"The second largest value is: {get_second_largest(arr)}")
