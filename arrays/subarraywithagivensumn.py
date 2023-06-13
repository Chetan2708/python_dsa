def subarray_with_sum(l, target_sum):
    current_sum = 0
    start = 0
    result = []

    for i in range(len(l)):
        current_sum += l[i]

        # If the current sum exceeds the target sum, move the start index
        # and subtract the element at start index from the current sum
        while current_sum > target_sum:
            current_sum -= l[start]
            start += 1

        # If the current sum matches the target sum, return True
        if current_sum == target_sum:
            return True

    # If no subarray is found, return -1
    return -1

l = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    l.append(element)

target_sum = int(input("Enter the target sum: "))
print(subarray_with_sum(l, target_sum))
