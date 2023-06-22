# def fun(l):
#     for i in range(len(l)):
#         if l[i]==x:
#             return(i)
#     return -1
def fun(l):
    low = 0
    high = len(l) - 1
    index = -1  # Initialize the index as -1
    while low <= high:
        mid = low + (high - low) // 2  # Calculate the middle index
        print(mid)
        if l[mid] == x:  # If the middle element is equal to the target value
            index = mid  # Update the index to the middle index
            high = mid - 1  # Adjust the high pointer to search for the leftmost occurrence
        if x > l[mid]:  # If the target value is greater than the middle element
            low = mid + 1  # Adjust the low pointer to search in the right half
        elif x < l[mid]:  # If the target value is less than the middle element
            high = mid - 1  # Adjust the high pointer to search in the left half
    return index

# Sorted array
l = [5, 10, 10, 10, 20, 20]
x = 10
print(fun(l))
